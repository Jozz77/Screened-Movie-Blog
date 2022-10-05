const modeToggle = document.querySelector(".mode-toggle");
const currentTheme = localStorage.getItem("theme");

if (currentTheme == "dark") {
  document.body.classList.add("lightmode");
}

modeToggle.addEventListener("click", () => {
  document.body.classList.toggle("lightmode");

  let theme = "light";
  if (document.body.classList.contains("lightmode")) {
    theme = "dark";
  }
  
  localStorage.setItem("theme", theme);
});
