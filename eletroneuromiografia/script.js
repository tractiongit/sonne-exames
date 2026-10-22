"use strict";

// Same event contract as the original exams page; a click is not a booked exam.
document.querySelectorAll("[data-cta-label]").forEach((link) => {
  link.addEventListener("click", () => {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: "cta_click",
      cta_label: link.dataset.ctaLabel,
      cta_url: link.href,
      page_path: window.location.pathname.replace(/\/?$/, "/"),
      landing_page: document.body.dataset.landingPage || "enmg_v1",
      exam: "eletroneuromiografia",
      unit: link.dataset.unit || "nao_selecionada",
      coverage: document.body.dataset.coverage || "nao_especificada",
    });
  });
});
