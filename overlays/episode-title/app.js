(() => {
  "use strict";

  const params = new URLSearchParams(window.location.search);
  const root = document.documentElement;
  const color = /^#[0-9a-f]{6}$/i;
  const setColor = (name, value) => {
    if (value && color.test(value)) root.style.setProperty(name, value);
  };

  document.getElementById("eyebrow").textContent = params.get("eyebrow") || "Remote podcast";
  document.getElementById("title").textContent = params.get("title") || "Episode title";
  document.getElementById("subtitle").textContent = params.get("subtitle") || "Optional subtitle";
  setColor("--accent", params.get("accent"));
  setColor("--text", params.get("text"));
})();
