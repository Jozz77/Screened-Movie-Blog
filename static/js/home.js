// elements for the timeline section
const progress = document.querySelector(".progress");
const timelineImgs = document.querySelectorAll(".timeline-image");
const timelineContainer = document.querySelector(".timeline-container");
const trailers = document.querySelectorAll(".trailer");
const progressSteps = document.querySelectorAll(".progress-step");
let imgNum = 0;
let trailerNum = 0;

// getting index of each image on hover
timelineImgs.forEach((img, index) => {
  img.addEventListener("mouseenter", () => {
    imgNum = index;
  });
});

// updating timeline and progress bar on hover of each image
timelineImgs.forEach((img) => {
  img.addEventListener("mouseenter", () => {
    updateTimeline();
    updateProgressbar();
  });
});

// removing progress bar and timeline on mouse out
timelineImgs.forEach((img) => {
  img.addEventListener("mouseout", () => {
    img.classList.remove("img-active");
    // removeProgressBar();
  });
});

// function controlling the timeline i.e the scaling of images
function updateTimeline() {
  timelineImgs.forEach((img) => {
    if (img.classList.contains("img-active")) {
      img.classList.remove("img-active");
    }
  });

  timelineImgs[imgNum].classList.add("img-active");
}

// function controlling the progress bar
function updateProgressbar() {
  // implementation of bubble progression
  progressSteps.forEach((step, idx) => {
    if (idx < imgNum + 1) {
      step.classList.add("progress-step-active");
    } else {
      step.classList.remove("progress-step-active");
    }
  });

  // implementation of line progression
  const progressActive = document.querySelectorAll(".progress-step-active");
  progress.style.width =
    ((progressActive.length - 1) / (timelineImgs.length - 1)) * 100 + "%";
}

// function removing progressbar
function removeProgressBar() {
  progressSteps.forEach((step) => {
    step.classList.remove("progress-step-active");
  });

  progressSteps[0].classList.add("progress-step-active");
  progress.style.width = "0%";
}

// IMPLEMENTATION OF TRAILER SECTION
timelineImgs.forEach((img) => {
  img.addEventListener("click", () => {
    trailers.forEach((trailer, index) => {
      index = imgNum;
      trailerNum = index;
      console.log(trailerNum);

      if (trailer.classList.contains("trailer-active")) {
        trailer.classList.remove("trailer-active");
      }
    });

    trailers[trailerNum].classList.add("trailer-active");
  });
});

// timelineImgs.forEach((img) => {
//   img.addEventListener("click", () => {});
// });
