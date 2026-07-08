import os
import re
import sys
from urllib.parse import urljoin, urlparse, urlunparse, unquote
from pathlib import Path
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://clinicasonne.com.br/exames-sonne/"
ROOT_DIR = Path(__file__).parent.resolve()
ASSETS_DIR = ROOT_DIR / "assets"
OUTPUT_HTML = ROOT_DIR / "index.html"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0 Safari/537.36"
    )
}

session = requests.Session()
session.headers.update(HEADERS)

# Keep track of downloaded resources to avoid duplicates.
downloaded = {}  # original_url -> local_relative_path
# Track the original URL of each downloaded CSS file so url() inside CSS is resolved correctly.
css_origins = {}  # local_relative_path -> original_absolute_url


def safe_filename(url: str) -> str:
    """Convert a URL into a safe local filename while preserving extension."""
    parsed = urlparse(url)
    path = unquote(parsed.path)
    if not path or path.endswith("/"):
        path = "index"
    # Remove leading slash
    path = path.lstrip("/")
    # Flatten path to a single filename, but keep the basename and extension
    base = Path(path).name
    if not base:
        base = "resource"
    # Clean query for cache-busting; keep it as part of filename if needed
    query = unquote(parsed.query)
    if query:
        # Shorten query to avoid extremely long names
        q = re.sub(r"[^a-zA-Z0-9_-]", "_", query)[:30]
        base_name, ext = os.path.splitext(base)
        base = f"{base_name}_{q}{ext}"
    # Ensure safe characters
    safe = re.sub(r"[^a-zA-Z0-9_.-]", "_", base)
    return safe


def local_path_for(url: str, content_type: str = "") -> Path:
    """Decide which local folder and extension an asset should have."""
    parsed = urlparse(url)
    path = parsed.path.lower()
    content_type = (content_type or "").lower().split(";")[0].strip()

    # Determine type/extension from URL first, then fall back to Content-Type
    if path.endswith(".css") or content_type == "text/css":
        folder = ASSETS_DIR / "css"
        ext = ".css"
    elif path.endswith(".js") or content_type in (
        "text/javascript",
        "application/javascript",
        "application/x-javascript",
    ):
        folder = ASSETS_DIR / "js"
        ext = ".js"
    elif path.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp")) or content_type.startswith("image/"):
        folder = ASSETS_DIR / "images"
        ext = Path(path).suffix if Path(path).suffix else "." + content_type.split("/")[-1] if content_type.startswith("image/") else ""
    elif path.endswith((".woff", ".woff2", ".ttf", ".otf", ".eot")) or content_type.startswith("font/"):
        folder = ASSETS_DIR / "fonts"
        ext = Path(path).suffix if Path(path).suffix else "." + content_type.split("/")[-1] if content_type.startswith("font/") else ""
    elif content_type == "text/html":
        folder = ASSETS_DIR / "other"
        ext = ".html"
    else:
        folder = ASSETS_DIR / "other"
        ext = ""

    folder.mkdir(parents=True, exist_ok=True)
    filename = safe_filename(url)

    # Add a sensible extension if the URL has none and Content-Type told us the type
    if ext and not Path(filename).suffix:
        filename = filename + ext

    return folder / filename


def download(url: str) -> str:
    """Download a resource and return its relative path from ROOT_DIR."""
    if url in downloaded:
        return downloaded[url]

    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"[ERRO] Não foi possível baixar {url}: {e}", file=sys.stderr)
        return url

    content_type = response.headers.get("content-type", "")
    local_file = local_path_for(url, content_type)
    local_file.write_bytes(response.content)
    relative = local_file.relative_to(ROOT_DIR).as_posix()
    downloaded[url] = relative
    print(f"[OK] {url} -> {relative}")
    return relative


def rewrite_url(url: str, base_url: str) -> str:
    """Convert an original URL to the downloaded local path."""
    if not url or url.startswith("#") or url.startswith("data:") or url.startswith("javascript:"):
        return url
    absolute = urljoin(base_url, url)
    # Keep mailto: and tel: untouched
    if absolute.startswith(("mailto:", "tel:")):
        return absolute
    # Download and return local path
    return download(absolute)


def process_html():
    """Fetch the page, download assets, rewrite HTML, and save it."""
    print(f"\nBaixando página base: {BASE_URL}")
    html = session.get(BASE_URL, timeout=30).text

    soup = BeautifulSoup(html, "html.parser")

    # Tags and attributes that can contain URLs
    asset_attrs = {
        "link": ["href"],
        "script": ["src", "data-rocket-src"],
        "img": ["src", "data-src", "data-lazy-src", "srcset", "data-srcset", "data-lazy-srcset"],
        "source": ["src", "srcset"],
        "audio": ["src"],
        "video": ["src", "poster"],
        "iframe": ["src", "data-lazy-src"],
        "embed": ["src"],
        "object": ["data"],
        "a": ["href"],          # mostly internal navigation / whatsapp links
        "input": ["src"],
    }

    for tag, attrs in asset_attrs.items():
        for node in soup.find_all(tag):
            for attr in attrs:
                value = node.get(attr)
                if not value:
                    continue

                if attr in ("srcset", "data-srcset", "data-lazy-srcset"):
                    # srcset: "url1 1x, url2 2x"
                    parts = []
                    for descriptor in value.split(","):
                        descriptor = descriptor.strip()
                        if not descriptor:
                            continue
                        tokens = descriptor.split()
                        if tokens:
                            url = tokens[0]
                            local = rewrite_url(url, BASE_URL)
                            tokens[0] = local
                            parts.append(" ".join(tokens))
                    node[attr] = ", ".join(parts)
                else:
                    node[attr] = rewrite_url(value, BASE_URL)
                    # Remember the original URL of every CSS file so background/font URLs inside it are resolved correctly.
                    if tag == "link" and attr == "href":
                        rel = node.get("rel", [])
                        if isinstance(rel, str):
                            rel = rel.split()
                        if "stylesheet" in rel or ("preload" in rel and node.get("as") == "style"):
                            css_origins[node[attr]] = urljoin(BASE_URL, value)

    # Inline styles with url()
    for node in soup.find_all(style=True):
        node["style"] = process_css_text(node["style"], BASE_URL)

    # Inline <style> blocks
    for style in soup.find_all("style"):
        if style.string:
            style.string = process_css_text(style.string, BASE_URL)

    # Process each discovered CSS file with its original URL as base.
    for local_path, original_url in css_origins.items():
        process_css_file(local_path, original_url)

    # Convert lazy-loaded images to direct src/srcset so they render without depending on JS lazy loaders.
    for img in soup.find_all("img"):
        if img.get("data-lazy-src"):
            img["src"] = img["data-lazy-src"]
            del img["data-lazy-src"]
        if img.get("data-lazy-srcset"):
            img["srcset"] = img["data-lazy-srcset"]
            del img["data-lazy-srcset"]
        if img.get("data-lazy-sizes"):
            img["sizes"] = img["data-lazy-sizes"]
            del img["data-lazy-sizes"]
    # Remove noscript image fallbacks that are now redundant.
    for noscript in soup.find_all("noscript"):
        content = noscript.decode_contents().strip()
        if content.startswith("<img"):
            noscript.decompose()

    # Elementor hides background images of lazy-loaded containers.
    # Add the class that marks them as loaded so hero/cards backgrounds show immediately.
    for node in soup.find_all(class_="e-con"):
        classes = node.get("class", [])
        if "e-parent" in classes and "e-lazyloaded" not in classes:
            classes.append("e-lazyloaded")
            node["class"] = classes

    # Preconnect / DNS-prefetch can be kept as-is because they are just hints
    # but for a true offline clone we can rewrite them too. Skipping to keep it simple.

    OUTPUT_HTML.write_text(str(soup), encoding="utf-8")
    print(f"\nHTML salvo em: {OUTPUT_HTML}")


def process_css_text(css_text: str, base_url: str, target_dir: Path = None) -> str:
    """Rewrite url(...) references inside CSS text.

    When *target_dir* is given (e.g. the directory of a CSS file), the
    resulting local paths are made relative to that directory so that
    browsers resolve them correctly.
    """
    pattern = re.compile(r"url\(\s*['\"]?([^'\"\)]+)['\"]?\s*\)")

    def replacer(match):
        url = match.group(1).strip()
        if url.startswith("data:") or url.startswith("#"):
            return match.group(0)
        local = rewrite_url(url, base_url)
        if target_dir is not None:
            local_file = ROOT_DIR / local
            local = os.path.relpath(local_file, target_dir).replace(os.sep, "/")
        return f"url({local})"

    return pattern.sub(replacer, css_text)


def process_css_file(relative_path: str, base_url: str):
    """Rewrite url() references inside downloaded CSS files."""
    css_file = ROOT_DIR / relative_path
    if not css_file.exists():
        return

    original_css = css_file.read_text(encoding="utf-8", errors="ignore")
    # Find original absolute URL for this CSS from downloaded mapping
    original_url = None
    for orig, rel in downloaded.items():
        if rel == relative_path:
            original_url = orig
            break
    css_base = original_url or base_url

    target_dir = css_file.parent
    rewritten_css = process_css_text(original_css, css_base, target_dir)
    css_file.write_text(rewritten_css, encoding="utf-8")


def main():
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    process_html()
    print("\nClone concluído.")


if __name__ == "__main__":
    main()
