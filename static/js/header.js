const modeToggle = document.querySelector(".mode-toggle");
const moon = document.querySelector(".moon");
const currentTheme = localStorage.getItem("theme");
const currentIcon = localStorage.getItem("icon");
const searchIcon = document.querySelector(".navigation__search");
const searchIcon2 = document.querySelector(".search-icon");
const searchIconMobile = document.querySelector(".navigation__search--mobile");
const searchBar = document.querySelector(".search-bar");
const clearBtn = document.querySelector(".clear-btn");
const searchInput = document.querySelector(".search-bar__input");
const overlay = document.querySelector(".overlay");
const preloader = document.querySelector(".preloader");
const allSearchIcons = [searchIcon, searchIcon2, searchIconMobile];

if (currentTheme == "dark") {
  document.body.classList.add("lightmode");
}
if (currentIcon == "moonIcon") {
  moon.classList.add("bi-sun");
}

modeToggle.addEventListener("click", () => {
  document.body.classList.toggle("lightmode");
  moon.classList.toggle("bi-sun");

  let theme = "light";
  if (document.body.classList.contains("lightmode")) {
    theme = "dark";
  }
  let icon = "sunIcon";
  if (moon.classList.contains("bi-sun")) {
    icon = "moonIcon";
  }

  localStorage.setItem("theme", theme);
  localStorage.setItem("icon", icon);
});

// implementation of search bar
// desktop search icon click, mobile search icon click and implementing search  bar remove on search icon inside search bar
allSearchIcons.forEach((icon) => {
  icon.addEventListener("click", () => {
    searchBar.classList.toggle("search-active");
    overlay.classList.toggle("active");
  });
});

// implementing clear button on search bar
clearBtn.addEventListener("click", () => {
  searchInput.value = "";
});

// implementing search bar remove on overlay click
overlay.addEventListener("click", () => {
  searchBar.classList.remove("search-active");
  overlay.classList.remove("active");
});

// implementing search bar remove on enter
searchInput.addEventListener("keyup", (e) => {
  if (e.keyCode === 13 && searchBar.classList.contains("search-active")) {
    searchBar.classList.remove("search-active");
  }
  if (e.key === "Enter" && searchBar.classList.contains("search-active")) {
    searchBar.classList.remove("search-active");
  }
});

// PRELOADER ANIMATION
window.addEventListener("load", () => {
  preloader.classList.add("preloader-hidden");
});

// Gsap animation for preloader
let tl = gsap.timeline({ repeat: -1, yoyo: true });
tl.from(".load-text", {
  duration: 1,
  opacity: 0,
  y: 300,
  stagger: 0.1,
  ease: "back",
});
