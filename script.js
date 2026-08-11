(() => {
  const config = window.STRATEGY_BAG_CONFIG || {};
  const menuButton = document.querySelector(".mobile-menu");
  const nav = document.querySelector(".site-nav");

  if (menuButton && nav) {
    menuButton.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      menuButton.setAttribute("aria-expanded", String(open));
    });
    nav.querySelectorAll("a").forEach(link => link.addEventListener("click", () => nav.classList.remove("open")));
  }

  const email = config.email || "";
  const subject = encodeURIComponent(config.consultationSubject || "STRATEGY BAG consultation inquiry");
  document.querySelectorAll(".contact-link").forEach(link => {
    link.href = `mailto:${email}?subject=${subject}`;
  });

  const linkedin = document.querySelector(".linkedin-link");
  if (linkedin) linkedin.href = config.linkedin || "#";

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  const insightGrid = document.getElementById("insight-grid");
  const visualClasses = ["visual-ai", "visual-brand", "visual-innovation"];

  function createInsightCard(item, index) {
    const card = document.createElement("article");
    card.className = "insight-card";

    const visual = document.createElement("div");
    visual.className = `insight-visual ${visualClasses[index] || visualClasses[0]}`;

    const tag = document.createElement("p");
    tag.className = "insight-tag";
    tag.textContent = item.category || "INSIGHT";

    const title = document.createElement("h3");
    title.textContent = item.title || "";

    const meta = document.createElement("p");
    meta.className = "insight-meta";
    meta.textContent = [item.source, item.date].filter(Boolean).join(" · ");

    const summary = document.createElement("p");
    summary.className = "insight-summary";
    summary.textContent = item.summary || "";

    card.append(visual, tag, title, meta, summary);

    if (item.url && item.url !== "#") {
      const link = document.createElement("a");
      link.href = item.url;
      link.target = "_blank";
      link.rel = "noopener";
      link.textContent = "Read article →";
      card.appendChild(link);
    }
    return card;
  }

  fetch("insights.json", { cache: "no-store" })
    .then(response => {
      if (!response.ok) throw new Error("Insight data unavailable");
      return response.json();
    })
    .then(items => {
      if (!Array.isArray(items) || items.length === 0) return;
      insightGrid.innerHTML = "";
      items.slice(0, 3).forEach((item, index) => insightGrid.appendChild(createInsightCard(item, index)));
    })
    .catch(() => {});
})();
