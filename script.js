(() => {
  const cfg = window.STRATEGY_BAG_CONFIG || {};
  const menu = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".main-nav");

  if (menu && nav) {
    menu.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      menu.setAttribute("aria-expanded", String(open));
    });
    nav.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        nav.classList.remove("open");
        menu.setAttribute("aria-expanded", "false");
      });
    });
  }

  const email = cfg.email || "";
  const subject = encodeURIComponent(cfg.consultationSubject || "STRATEGY BAG consultation inquiry");
  document.querySelectorAll(".contact-link").forEach(link => {
    link.href = `mailto:${email}?subject=${subject}`;
  });

  const linkedin = document.querySelector(".linkedin-link");
  if (linkedin) linkedin.href = cfg.linkedin || "#";

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  const grid = document.getElementById("insight-grid");
  const visuals = ["ai-visual","brand-visual","innovation-visual"];

  function createCard(item,index){
    const card = document.createElement("article");
    card.className = "insight-card";
    card.innerHTML = `
      <div class="insight-visual ${visuals[index] || visuals[0]}"></div>
      <p class="tag">${item.category || "INSIGHT"}</p>
      <h3>${item.title || ""}</h3>
      <p class="insight-meta">${[item.source,item.date].filter(Boolean).join(" · ")}</p>
      <p class="insight-summary">${item.summary || ""}</p>
      ${item.url && item.url !== "#" ? `<a href="${item.url}" target="_blank" rel="noopener">Read article →</a>` : ""}
    `;
    return card;
  }

  fetch("insights.json",{cache:"no-store"})
    .then(r => {
      if(!r.ok) throw new Error("insights unavailable");
      return r.json();
    })
    .then(items => {
      if(!Array.isArray(items) || items.length < 3) return;
      grid.innerHTML="";
      items.slice(0,3).forEach((item,index) => grid.appendChild(createCard(item,index)));
    })
    .catch(() => {});
})();
