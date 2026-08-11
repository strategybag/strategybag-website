(() => {
  const cfg = window.STRATEGY_BAG_CONFIG || {};
  const menu = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".site-nav");

  if (menu && nav) {
    menu.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      menu.setAttribute("aria-expanded", String(open));
    });
  }

  const email = cfg.email || "";
  const subject = encodeURIComponent(cfg.consultationSubject || "STRATEGY BAG consultation inquiry");
  document.querySelectorAll(".contact-link").forEach(link => {
    link.href = `mailto:${email}?subject=${subject}`;
  });

  const li = document.querySelector(".linkedin-link");
  if (li) li.href = cfg.linkedin || "#";

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  const grid = document.getElementById("insight-grid");
  const visualClasses = ["ai-visual","brand-visual","innovation-visual"];

  function makeCard(item, i){
    const card = document.createElement("article");
    card.className = "insight-card";
    card.innerHTML = `
      <div class="insight-visual ${visualClasses[i] || visualClasses[0]}"></div>
      <p class="tag">${item.category || "INSIGHT"}</p>
      <h3>${item.title || ""}</h3>
      <p style="margin-top:0;color:#58677a;font-size:11px">${[item.source,item.date].filter(Boolean).join(" · ")}</p>
      <p style="color:#58677a;font-size:11px">${item.summary || ""}</p>
      ${item.url && item.url !== "#" ? `<a href="${item.url}" target="_blank" rel="noopener" style="display:inline-block;margin:6px 15px 0;color:#00723f;font-size:11px;font-weight:800;text-decoration:none">Read article →</a>` : ""}
    `;
    return card;
  }

  fetch("insights.json", {cache:"no-store"})
    .then(r => r.json())
    .then(items => {
      if (!Array.isArray(items) || items.length < 3) return;
      grid.innerHTML = "";
      items.slice(0,3).forEach((item,i) => grid.appendChild(makeCard(item,i)));
    })
    .catch(() => {});
})();
