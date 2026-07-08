# Diretrizes da Marca — Clínica Sonne

## Identidade
A Clínica Sonne é uma clínica de neurologia premium. A comunicação visual deve transmitir:
- **Confiança e precisão médica**
- **Tecnologia de ponta**
- **Acolhimento e cuidado**
- **Profissionalismo e modernidade**

---

## Paleta de Cores

| Token | Hex | Uso |
|-------|-----|-----|
| **Azul escuro** | `#122353` | Fundos de seções escuras, títulos principais, navegação, rodapés |
| **Azul claro** | `#9DC9F7` | Subtítulos, destaques em fundo escuro, ícones secundários |
| **Azul gelo** | `#C9DDEF` | Cards suaves, fundos alternativos, divisores leves |
| **Verde** | `#43AD51` | Botões de CTA (WhatsApp), ações principais, estados de sucesso |
| **Branco** | `#FFFFFF` | Texto sobre fundos escuros, fundos claros, espaços em branco |
| **Preto** | `#000000` | Texto primário em fundos claros (quando necessário) |

### Regras de uso
- **CTAs devem ser verdes** (`#43AD51`) para gerar contraste e ação.
- **Texto sobre azul escuro deve ser branco** ou azul claro (`#9DC9F7`).
- **Não usar texto escuro sobre azul escuro** — compromete a legibilidade.
- **Fotos de exames/corpo clínico** devem ter leve tratamento azulado para manter a coerência com a paleta.

---

## Tipografia

| Função | Fonte | Peso | Tamanho-base | Uso |
|--------|-------|------|--------------|-----|
| **Headlines** | Montserrat | 600 | 32–42px | Títulos de seção, hero |
| **Subtítulos** | Montserrat | 400–600 | 18–26px | Descrições de seção, títulos de cards |
| **Corpo** | Montserrat | 400–500 | 15–18px | Parágrafos, listas de exames |
| **Botões** | Montserrat | 600 | 14–18px | CTAs e links de ação |
| **Legendas** | Montserrat | 400 | 12–14px | Endereços, horários, créditos |

### Regras de uso
- **Letra condensada (tracking negativo):** headlines podem usar `letter-spacing: -0.3px` a `-1.4px` para um ar mais moderno.
- **Linha de título:** `line-height: 1.2em` para títulos grandes.
- **Contraste obrigatório:** manter o texto sempre legível sobre o fundo escolhido.

---

## Estilo Visual Geral

### Layout
- Páginas em **seções largas e empilhadas** (full-width sections).
- **Cards com cantos arredondados** (border-radius ~22px) para os blocos de conteúdo em destaque.
- Espaçamento generoso entre seções: `padding: 50px 0` no mínimo para headlines.
- Uso de **imagens decorativas em fundos** (elipses, ondas suaves) para criar profundidade sem poluir.

### Botões
- **Formato:** bordas arredondadas, ícone à esquerda (WhatsApp) + texto.
- **Cor padrão:** `#43AD51` com texto branco.
- **Hover:** leve escurecimento do verde (ex: `#3A9A47`).
- **Alinhamento:** centralizado em seções de conversão; à esquerda em blocos de texto.

### Imagens
- **Ícones:** linha fina, estilo Material/Fluent, em branco ou azul claro quando sobre fundo escuro.
- **Fotografia:** clínica limpa, luz natural, pacientes e médicos em ambiente profissional. Preferir tom azulado.
- **Ilustrações decorativas:** elipses transparentes e ondas suaves nas cores da marca.

---

## Tom de Voz
- **Profissional, mas acolhedor.**
- **Claro e objetivo:** evitar jargão médico excessivo; quando necessário, explicar o exame de forma simples.
- **Empoderador:** "A hora de ser cuidada", "Agende seu exame", "Cuide da sua saúde".
- **Confiança:** evidenciar tecnologia de ponta e equipe especializada.

---

## Boas Práticas de Responsividade

- **Mobile-first:** garantir que todos os blocos de texto sejam legíveis em telas pequenas.
- **Margens fixas grandes devem ser reduzidas** em breakpoints (`max-width: 1024px` e `max-width: 767px`).
- **CTAs principais devem ser visíveis sem scroll excessivo** no mobile.
- **Mapas e endereços:** empilhar verticalmente em telas estreitas.

---

## Arquivos de Referência no Projeto

- Estilos principais: `assets/css/post-3120_ver_1782871379.css`
- Página: `index.html`
- Fonte: `assets/css/css_family_Roboto_100_100italic_20.css` (arquivo local do Google Fonts — Montserrat/Roboto)

---

## Aplicação: Página de Exames Neurológicos

Página construída seguindo as diretrizes acima — identidade premium, cores da marca, tipografia Montserrat e CTAs verdes.

<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exames Neurológicos — Clínica Sonne</title>
  <meta name="description" content="Diagnóstico neurológico de alta precisão em Campinas e Hortolândia. Eletroneuromiografia, EEG, potenciais evocados e ultrassom neuromuscular na Clínica Sonne.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --azul-escuro: #122353;
      --azul-claro: #9DC9F7;
      --azul-gelo: #C9DDEF;
      --verde: #43AD51;
      --verde-hover: #3A9A47;
      --branco: #FFFFFF;
      --preto: #1A1A1A;
      --cinza: #5A5A5A;
      --bg-suave: #F8FAFD;
      --radius: 22px;
      --radius-btn: 32px;
      --max-width: 1140px;
      --space: 80px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Montserrat', sans-serif;
      color: var(--preto);
      line-height: 1.6;
      background: var(--branco);
    }

    img { max-width: 100%; display: block; }

    a { text-decoration: none; color: inherit; }

    .container {
      width: 92%;
      max-width: var(--max-width);
      margin: 0 auto;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: var(--verde);
      color: var(--branco);
      font-weight: 600;
      font-size: 15px;
      padding: 14px 28px;
      border-radius: var(--radius-btn);
      transition: all 0.25s ease;
      box-shadow: 0 4px 14px rgba(67, 173, 81, 0.28);
    }

    .btn:hover {
      background: var(--verde-hover);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(67, 173, 81, 0.35);
    }

    .btn svg { width: 20px; height: 20px; fill: currentColor; }

    .section { padding: var(--space) 0; }

    .section-dark {
      background: var(--azul-escuro);
      color: var(--branco);
      position: relative;
      overflow: hidden;
    }

    .section-dark::before {
      content: '';
      position: absolute;
      top: -80px;
      right: -120px;
      width: 420px;
      height: 420px;
      background: radial-gradient(circle, rgba(157, 201, 247, 0.14) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    .section-gelo { background: var(--bg-suave); }

    h1, h2, h3 {
      font-weight: 600;
      line-height: 1.2;
      letter-spacing: -0.5px;
    }

    h1 { font-size: 42px; }
    h2 { font-size: 34px; }
    h3 { font-size: 24px; }

    p { margin-bottom: 16px; }
    p:last-child { margin-bottom: 0; }

    ul { list-style: none; padding: 0; }
    ul li {
      position: relative;
      padding-left: 22px;
      margin-bottom: 10px;
      color: var(--cinza);
    }
    ul li::before {
      content: '';
      position: absolute;
      left: 0;
      top: 10px;
      width: 7px;
      height: 7px;
      background: var(--verde);
      border-radius: 50%;
    }

    .section-dark ul li { color: rgba(255, 255, 255, 0.85); }
    .section-dark ul li::before { background: var(--azul-claro); }

    .badge {
      display: inline-block;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--azul-claro);
      margin-bottom: 16px;
    }

    .hero {
      min-height: 92vh;
      display: flex;
      align-items: center;
      background:
        linear-gradient(110deg, rgba(18, 35, 83, 0.96) 0%, rgba(18, 35, 83, 0.88) 55%, transparent 100%),
        url('assets/images/5af950d3-bg_1000000000000000000028.png') center/cover no-repeat;
    }

    .hero .container { position: relative; z-index: 1; }

    .hero h1 {
      color: var(--branco);
      max-width: 700px;
      margin-bottom: 20px;
    }

    .hero p {
      color: rgba(255, 255, 255, 0.88);
      font-size: 18px;
      max-width: 620px;
      margin-bottom: 32px;
    }

    .intro-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      align-items: center;
    }

    .intro-text h2 {
      color: var(--azul-escuro);
      margin-bottom: 20px;
    }

    .intro-text p { color: var(--cinza); font-size: 17px; }

    .photos {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    .photo-card {
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(18, 35, 83, 0.1);
      background: var(--azul-gelo);
      min-height: 240px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 20px;
      color: var(--azul-escuro);
      font-weight: 500;
      font-size: 14px;
    }

    .photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .exames-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }

    .exame-card {
      background: var(--branco);
      border-radius: var(--radius);
      padding: 36px;
      box-shadow: 0 6px 22px rgba(18, 35, 83, 0.08);
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .exame-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(18, 35, 83, 0.14);
    }

    .exame-card h3 {
      color: var(--azul-escuro);
      margin-bottom: 14px;
    }

    .exame-card p { color: var(--cinza); font-size: 15px; margin-bottom: 18px; }
    .exame-card strong { color: var(--azul-escuro); }
    .exame-card .btn { margin-top: 10px; }

    .section-header {
      text-align: center;
      max-width: 760px;
      margin: 0 auto 48px;
    }

    .section-header h2 { color: var(--azul-escuro); margin-bottom: 14px; }
    .section-dark .section-header h2 { color: var(--branco); }
    .section-header p { color: var(--cinza); font-size: 17px; }
    .section-dark .section-header p { color: rgba(255, 255, 255, 0.8); }

    .specialists {
      text-align: center;
      max-width: 900px;
      margin: 0 auto;
      font-size: 18px;
      line-height: 1.7;
      color: rgba(255, 255, 255, 0.9);
    }

    .agende {
      text-align: center;
      max-width: 800px;
      margin: 0 auto;
    }

    .agende p { color: var(--cinza); font-size: 17px; }

    .unidades {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      text-align: left;
      margin-top: 40px;
    }

    .unidade {
      background: var(--branco);
      border-radius: var(--radius);
      padding: 28px;
      box-shadow: 0 6px 22px rgba(18, 35, 83, 0.08);
    }

    .unidade strong {
      display: block;
      color: var(--azul-escuro);
      font-size: 18px;
      margin-bottom: 8px;
    }

    .unidade p { color: var(--cinza); font-size: 15px; margin: 0; }

    .horario {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--azul-escuro);
      color: var(--branco);
      padding: 12px 22px;
      border-radius: var(--radius-btn);
      font-size: 14px;
      font-weight: 500;
      margin-top: 24px;
    }

    .footer-mini {
      background: #0C1839;
      color: rgba(255, 255, 255, 0.7);
      text-align: center;
      padding: 24px 0;
      font-size: 13px;
    }

    @media (max-width: 1024px) {
      :root { --space: 60px; }
      h1 { font-size: 36px; }
      h2 { font-size: 30px; }
      .intro-grid, .exames-grid, .unidades { grid-template-columns: 1fr; }
    }

    @media (max-width: 767px) {
      :root { --space: 48px; }
      h1 { font-size: 30px; }
      h2 { font-size: 26px; }
      h3 { font-size: 21px; }
      .hero { min-height: auto; padding: 80px 0 60px; }
      .photos { grid-template-columns: 1fr; }
      .exame-card { padding: 26px; }
      .btn { width: 100%; }
    }
  </style>
</head>
<body>

  <!-- Hero -->
  <section class="hero section-dark">
    <div class="container">
      <span class="badge">Neurologia Premium</span>
      <h1>Diagnóstico Neurológico de Alta Precisão em Campinas e Hortolândia</h1>
      <p>Realize seus exames neurológicos na Clínica Sonne com agilidade, tecnologia de ponta e o suporte de uma equipe de especialistas. Tem um encaminhamento em mãos? Agende seu horário de forma simples e rápida.</p>
      <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Tenho%20um%20encaminhamento%20e%20quero%20agendar%20meu%20exame%20neurol%C3%B3gico%20na%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
        Agendar meu Exame Neurológico
      </a>
    </div>
  </section>

  <!-- Introdução -->
  <section class="section">
    <div class="container">
      <div class="intro-grid">
        <div class="intro-text">
          <h2>A saúde não pode esperar</h2>
          <p>Na Clínica Sonne, estamos comprometidos em fornecer um atendimento médico excepcional e abrangente para você e sua família. Com uma equipe altamente qualificada e equipamentos modernos, oferecemos uma gama completa de exames médicos para cuidar da sua saúde neurológica e mental.</p>
          <p>Somos referência em exames neurológicos nas unidades de Campinas e Hortolândia. Independentemente da complexidade do seu caso, estamos aqui para oferecer um diagnóstico preciso e um tratamento eficaz.</p>
          <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Quero%20agendar%20um%20exame%20na%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
            Agendar o exame!
          </a>
        </div>
        <div class="photos">
          <div class="photo-card">
            <span>[Inserir Foto Real da Sala de Exames — Unidade Campinas]</span>
          </div>
          <div class="photo-card">
            <span>[Inserir Foto Real da Sala de Exames — Unidade Hortolândia]</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Exames -->
  <section class="section section-gelo">
    <div class="container">
      <div class="section-header">
        <h2>Confira os exames realizados pela Clínica Sonne</h2>
        <p>Exames modernos, precisos e realizados por especialistas em neurofisiologia clínica.</p>
      </div>
      <div class="exames-grid">
        <article class="exame-card">
          <h3>Eletroneuromiografia</h3>
          <p>A eletroneuromiografia é um exame complementar que consiste em um conjunto de testes diagnósticos para avaliar a função do sistema nervoso periférico: nervos, músculos e junção neuromuscular.</p>
          <p><strong>Exames disponíveis:</strong></p>
          <ul>
            <li>Membros superiores</li>
            <li>Membros inferiores</li>
            <li>4 membros</li>
            <li>Fibra única</li>
            <li>Avaliação de transtornos do movimento</li>
            <li>Segmento complementar ou especial</li>
          </ul>
          <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Quero%20falar%20com%20um%20especialista%20sobre%20eletroneuromiografia%20na%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
            Fale com um especialista!
          </a>
        </article>

        <article class="exame-card">
          <h3>Eletroencefalograma (EEG)</h3>
          <p>O exame eletroencefalograma permite correlacionar as atividades elétricas cerebrais com eventos clínicos e comportamentais, auxiliando no diagnóstico de distúrbios neurológicos complexos.</p>
          <p><strong>Exames disponíveis:</strong></p>
          <ul>
            <li>EEG em sono e vigília (rotina)</li>
            <li>Vídeo EEG</li>
            <li>EEG prolongado</li>
            <li>EEG quantitativo (mapeamento cerebral)</li>
          </ul>
          <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Quero%20falar%20com%20um%20especialista%20sobre%20EEG%20na%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
            Fale com um especialista!
          </a>
        </article>

        <article class="exame-card">
          <h3>Potenciais Evocados</h3>
          <p>O exame de potencial evocado é uma técnica diagnóstica que avalia a atividade elétrica neurológica em resposta a estímulos sensoriais específicos, fornecendo informações sobre a integridade das vias neurais e o funcionamento do sistema nervoso central.</p>
          <p><strong>Exames disponíveis:</strong></p>
          <ul>
            <li>Potencial evocado visual</li>
            <li>Potencial evocado do tronco cerebral (PEATE, PEATC ou BERA)</li>
            <li>Potencial evocado somatossensitivo</li>
          </ul>
          <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Quero%20falar%20com%20um%20especialista%20sobre%20potenciais%20evocados%20na%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
            Fale com um especialista!
          </a>
        </article>

        <article class="exame-card">
          <h3>Ultrassom Neuromuscular</h3>
          <p>O ultrassom neuromuscular é um exame de imagem moderno, indolor e de alta precisão. Ele permite a visualização detalhada de nervos e músculos em tempo real, sendo frequentemente realizado em conjunto com a eletroneuromiografia para um diagnóstico ainda mais assertivo.</p>
          <p><strong>Aplicações e avaliações disponíveis:</strong></p>
          <ul>
            <li>Avaliação de compressões nervosas (ex: Síndrome do Túnel do Carpo)</li>
            <li>Análise detalhada de nervos periféricos</li>
            <li>Investigação de doenças musculares e miopatias</li>
            <li>Identificação de lesões ou traumas nos nervos</li>
            <li>Avaliação complementar e integrada no momento da consulta clínica</li>
          </ul>
          <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Quero%20falar%20com%20um%20especialista%20sobre%20ultrassom%20neuromuscular%20na%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
            Fale com um especialista!
          </a>
        </article>
      </div>
    </div>
  </section>

  <!-- Especialistas -->
  <section class="section section-dark">
    <div class="container">
      <div class="section-header">
        <h2>Especialistas fazem a experiência na Clínica Sonne ser eficiente e segura!</h2>
      </div>
      <div class="specialists">
        <p>Contamos com um corpo clínico e uma equipe técnica de excelência, formada por profissionais altamente qualificados em neurofisiologia clínica. Nossa equipe possui treinamentos nos principais centros de referência do país e certificações pelas principais sociedades médicas (como a SBNC). Nosso foco é garantir segurança, um atendimento humanizado e diagnósticos de altíssima precisão para todos os nossos pacientes.</p>
      </div>
    </div>
  </section>

  <!-- Agendamento -->
  <section class="section section-gelo">
    <div class="container">
      <div class="agende">
        <h2>Agende agora e cuide da sua saúde</h2>
        <p>Agende o exame na Clínica Sonne hoje mesmo e comece a jornada rumo ao bem-estar. Estamos ansiosos para ajudar quem precisa de exames a viver de forma mais saudável e plena!</p>
        <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Quero%20agendar%20um%20exame%20na%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
          Agendar o exame!
        </a>
        <div class="horario">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
          Horário de Atendimento: De segunda a sexta, das 08:00 às 17:00 horas.
        </div>
      </div>

      <div class="unidades">
        <div class="unidade">
          <strong>Campinas</strong>
          <p>Edifício Medplex — Av. Barão de Itapura, 610 — Sala 510 — Taquaral, SP, 13020-430</p>
        </div>
        <div class="unidade">
          <strong>Hortolândia</strong>
          <p>R. João Blumer, 289 — Remanso Campineiro, Hortolândia — SP, 13184-430</p>
        </div>
      </div>

      <div style="text-align: center; margin-top: 36px;">
        <p>Se precisar, fale diretamente com a nossa equipe:</p>
        <a class="btn" href="https://wa.me/5519996283086?text=Ol%C3%A1!%20Visitei%20o%20site%20e%20quero%20falar%20com%20a%20recep%C3%A7%C3%A3o%20da%20Cl%C3%ADnica%20Sonne" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.521.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.521.074-.797.372-.275.298-1.051 1.027-1.051 2.507 0 1.481 1.079 2.912 1.229 3.111.149.198 2.122 3.239 5.14 4.54.719.31 1.28.496 1.718.634.722.229 1.379.197 1.898.12.579-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.144 7.437h-.004c-1.107 0-2.192-.275-3.154-.8l-.226-.124-2.346.615.626-2.289-.147-.234c-.567-.904-.867-1.948-.867-3.021 0-3.206 2.608-5.813 5.814-5.813 1.552 0 3.011.606 4.107 1.705 1.096 1.1 1.699 2.558 1.699 4.108 0 3.206-2.609 5.813-5.815 5.813M12.001.8C5.49.8.4 5.889.4 12.4c0 2.186.572 4.318 1.655 6.195L.675 23.301l4.801-1.26c1.806.984 3.84 1.501 5.92 1.501h.005c6.512 0 11.8-5.289 11.8-11.8 0-3.152-1.227-6.117-3.455-8.344C18.123 1.77 15.158.8 12.001.8"/></svg>
          Fale com a Recepção
        </a>
      </div>
    </div>
  </section>

  <footer class="footer-mini">
    <div class="container">
      <p>&copy; 2026 Clínica Sonne — Neurologia Premium. Todos os direitos reservados.</p>
    </div>
  </footer>

</body>
</html>
