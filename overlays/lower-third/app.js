(() => {
  "use strict";

  const params = new URLSearchParams(window.location.search);
  const root = document.documentElement;
  const color = /^#[0-9a-f]{6}$/i;
  const setColor = (name, value) => {
    if (value && color.test(value)) root.style.setProperty(name, value);
  };

  document.getElementById("name").textContent = params.get("name") || "Guest name";
  document.getElementById("role").textContent = params.get("role") || "Role or organization";
  setColor("--accent", params.get("accent"));
  setColor("--text", params.get("text"));
})();
