const searchIcon = document.querySelector(".navigation__search");
const searchIcon2 = document.querySelector(".search-icon");
const searchIconMobile = document.querySelector(".navigation__search--mobile");
const searchBar = document.querySelector(".search-bar");
const clearBtn = document.querySelector(".clear-btn");
const searchInput = document.querySelector(".search-bar__input");
const overlay = document.querySelector(".overlay");
let preloader = document.querySelector(".preloader");
const homePage = document.querySelector(".home-page");
const navLogo = document.querySelector(".navigation__logo");
const navLogo_mobile = document.querySelector(".navigation__logo--mobile");
const allSearchIcons = [searchIcon, searchIcon2, searchIconMobile];

// preloader.classList.remove("preloader-hidden");

//  DON'T DELETE !!! MODE TOGGLE FUNCTIONALITY CODE
const whiteMode = document.querySelector("#white-mode");
const lightBlueMode = document.querySelector("#lightBlue-mode");
const darkBlueMode = document.querySelector("#darkBlue-mode");
const greyMode = document.querySelector("#grey-mode");
// const moon = document.querySelector(".moon");
const currentTheme = localStorage.getItem("theme");
// const currentIcon = localStorage.getItem("icon");
if (currentTheme == "white") {
  document.body.classList.add("white-mode");
}
if (currentTheme == "lightBlue") {
  document.body.classList.add("lightBlue-mode");
}
if (currentTheme == "darkBlue") {
  document.body.classList.add("darkBlue-mode");
}
if (currentTheme == "grey") {
  document.body.classList.add("grey-mode");
}

whiteMode.addEventListener("click", () => {
  document.body.setAttribute("class", "white-mode");
  let theme = "another";
  if (document.body.classList.contains("white-mode")) {
    theme = "white";
  }

  localStorage.setItem("theme", theme);
});
lightBlueMode.addEventListener("click", () => {
  document.body.setAttribute("class", "lightBlue-mode");

  let theme = "another";
  if (document.body.classList.contains("lightBlue-mode")) {
    theme = "lightBlue";
  }

  localStorage.setItem("theme", theme);
});
darkBlueMode.addEventListener("click", () => {
  document.body.setAttribute("class", "darkBlue-mode");

  let theme = "another";
  if (document.body.classList.contains("darkBlue-mode")) {
    theme = "darkBlue";
  }

  localStorage.setItem("theme", theme);
});
greyMode.addEventListener("click", () => {
  document.body.setAttribute("class", "grey-mode");

  let theme = "another";
  if (document.body.classList.contains("grey-mode")) {
    theme = "grey";
  }

  localStorage.setItem("theme", theme);
});

function themeFunction(e) {
  if (document.querySelector("#mode-toggle .toggle-box.shadow") !== null) {
    document.querySelector("#mode-toggle .toggle-box.shadow").classList.remove("shadow");
  }
  e.target.classList.add("shadow");
}

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

// // PRELOADER ANIMATION
// window.addEventListener("load", () => {
//   preloader.classList.add("preloader-hidden");
// });

// showing preloader on click
// homePage.addEventListener("click", () => {
//   preloader.classList.add("preloader-shown");
// });
// navLogo.addEventListener("click", () => {
//   preloader.classList.add("preloader-shown");
// });
// navLogo_mobile.addEventListener("click", () => {
//   preloader.classList.add("preloader-shown");
// });

// Gsap animation for preloader
let tl = gsap.timeline({ repeat: -1, yoyo: true });
tl.from(".load-text", {
  duration: 1,
  opacity: 0,
  y: "random(-300, 300)",
  stagger: 0.1,
  ease: "back",
});
