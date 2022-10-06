const modeToggle = document.querySelector(".mode-toggle");
const moon = document.querySelector(".moon");
const currentTheme = localStorage.getItem("theme");
const currentIcon = localStorage.getItem("icon");

if (currentTheme == "dark") {
  document.body.classList.add("lightmode");
}
if (currentIcon == 'moonIcon'){
  moon.classList.add("bi-sun");
}

modeToggle.addEventListener("click", () => {
  document.body.classList.toggle("lightmode");
  moon.classList.toggle("bi-sun");

  let theme = "light";
  if (document.body.classList.contains("lightmode")) {
    theme = "dark";
  }
  let icon = 'sunIcon';
  if (moon.classList.contains("bi-sun")) {
    icon = 'moonIcon';
  }

  localStorage.setItem("theme", theme);
  localStorage.setItem("icon", icon);
});
