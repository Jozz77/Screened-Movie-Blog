// "use strict";

// elements for the timeline section
const progress = document.querySelector(".progress");
const timelineImgs = document.querySelectorAll(".timeline-image");
const timelineTitle = document.querySelectorAll(".timeline-title");
const timelineContainer = document.querySelector(".timeline-container");
const trailers = document.querySelectorAll(".trailer");
const progressSteps = document.querySelectorAll(".progress-step");

let imgNum = 0;
let imgNumClick = 0;
let imgNumClick_Constant = 0;
let trailerNum = 0;
let imgClicked = false;

// getting index of each image on hover
timelineImgs.forEach((img, index) => {
  img.addEventListener("mouseenter", () => {
    imgNum = index;
  });
});

// getting index of each image on click and updating progressbar
timelineImgs.forEach((img, index) => {
  img.addEventListener("click", () => {
    imgNumClick = index;
    imgClicked = true;
    updateTitleClick();
    updateProgressbar();

    // IMPLEMENTATION OF TRAILER SECTION
    trailers.forEach((trailer, index) => {
      index = imgNumClick;
      trailerNum = index;

      if (trailer.classList.contains("trailer-active")) {
        trailer.classList.remove("trailer-active");
      }
    });
    trailers[trailerNum].classList.add("trailer-active");
  });
});

// updating timeline and progress bar on hover of each image
timelineImgs.forEach((img) => {
  img.addEventListener("mouseenter", () => {
    updateTitle();
    updateProgressbar_Hover();
  });
});

// updating progress bar and timeline on mouse out
timelineImgs.forEach((img) => {
  img.addEventListener("mouseout", () => {
    updateProgressbar();
    updateTitleClick();
  });
});

// functions controlling the titles i.e gold colors on click and hover
function updateTitle() {
  timelineTitle.forEach((title) => {
    if (title.classList.contains("title-active")) {
      title.classList.remove("title-active");
    }
  });

  timelineTitle[imgNum].classList.add("title-active");
}
function updateTitleClick() {
  timelineTitle.forEach((title) => {
    if (title.classList.contains("title-active")) {
      title.classList.remove("title-active");
    }
  });

  timelineTitle[imgNumClick].classList.add("title-active");
}

// function controlling the progress bar
function updateProgressbar() {
  // implementation of bubble progression
  progressSteps.forEach((step, idx) => {
    if (idx < imgNumClick + 1) {
      step.classList.add("progress-step-active");
    } else {
      step.classList.remove("progress-step-active");
    }
  });

  // implementation of line progression
  let progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (timelineImgs.length - 1)) * 100 + "%";
}
// updating progress bar on hover
function updateProgressbar_Hover() {
  // implementation of bubble progression
  progressSteps.forEach((step, idx) => {
    if (idx < imgNum + 1) {
      step.classList.add("progress-step-active");
    } else {
      step.classList.remove("progress-step-active");
    }
  });
  // implementation of line progression
  progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (timelineImgs.length - 1)) * 100 + "%";
}

// function removing progressbar
function removeProgressBar() {
  if (!imgClicked) {
    progressSteps.forEach((step, idx) => {
      if (idx < imgNum + 1) {
        step.classList.remove("progress-step-active");
      }
    });

    progressSteps[0].classList.add("progress-step-active");
    progress.style.width = "0%";
  }
}

// PRELOADER ANIMATION
window.addEventListener("load", () => {
  preloader.classList.remove("preloader-shown");
  preloader.classList.add("preloader-hidden");
});

// Gsap animation for preloader
// tl = gsap.timeline({ repeat: -1, yoyo: true });
// tl.from(".load-text", {
//   duration: 1,
//   opacity: 0,
//   y: 300,
//   stagger: 0.1,
//   ease: "back",
// });
