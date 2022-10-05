//getting the elements through DOM
// const hollywoodImage = document.querySelector("#hollywood-img");
// const hollywoodTrailer = document.querySelector("#hollywood-trailer");
// const hollywood = document.querySelector("#hollywood");

// const bollywoodImage = document.querySelector("#bollywood-img");
// const bollywoodTrailer = document.querySelector("#bollywood-trailer");
// const bollywood = document.querySelector("#bollywood");

// const nollywoodImage = document.querySelector("#nollywood-img");
// const nollywoodTrailer = document.querySelector("#nollywood-trailer");
// const nollywood = document.querySelector("#nollywood");

// const kDramasImage = document.querySelector("#kdramas-img");
// const kDramasTrailer = document.querySelector("#kdrama-trailer");
// const kdrama = document.querySelector("#k-dramas");

// const tvSeriesImage = document.querySelector("#tvseries-img");
// const tvSeriesTrailer = document.querySelector("#tvseries-trailer");
// const tvSeries = document.querySelector("#tv-series");

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
    updateTimeline();
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
    updateTimeline();
    updateProgressbar_Hover();
  });
});

// updating progress bar and timeline on mouse out
timelineImgs.forEach((img) => {
  img.addEventListener("mouseout", () => {
    updateProgressbar();
    timelineTitle.forEach((title) => {
      title.classList.remove("title-active");
    });
  });
});

// function controlling the timeline i.e the scaling of images
function updateTimeline() {
  timelineTitle.forEach((title) => {
    if (title.classList.contains("title-active")) {
      title.classList.remove("title-active");
    }
  });

  timelineTitle[imgNum].classList.add("title-active");
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

/*added a click event listener to the images to make the trailer 
box show when the image is clicked;
made sure other boxes weren't visible when the active one is and
removed the active class on the borders of inactive images
*/
// hollywoodImage.addEventListener("click", () => {
//   showTrailer(hollywoodTrailer, hollywood);

//   let otherTrailers = [
//     tvSeriesTrailer,
//     bollywoodTrailer,
//     nollywoodTrailer,
//     kDramasTrailer,
//   ];
//   let otherBorders = [tvSeries, bollywood, nollywood, kdrama];

//   otherTrailers.forEach(removeTrailer);
//   otherBorders.forEach(removeBorder);
// });

// bollywoodImage.addEventListener("click", () => {
//   showTrailer(bollywoodTrailer, bollywood);

//   let otherTrailers = [
//     hollywoodTrailer,
//     tvSeriesTrailer,
//     nollywoodTrailer,
//     kDramasTrailer,
//   ];
//   let otherBorders = [hollywood, tvSeries, nollywood, kdrama];

//   otherTrailers.forEach(removeTrailer);
//   otherBorders.forEach(removeBorder);
// });

// nollywoodImage.addEventListener("click", () => {
//   showTrailer(nollywoodTrailer, nollywood);

//   let otherTrailers = [
//     hollywoodTrailer,
//     bollywoodTrailer,
//     tvSeriesTrailer,
//     kDramasTrailer,
//   ];
//   let otherBorders = [hollywood, bollywood, kdrama, tvSeries];

//   otherTrailers.forEach(removeTrailer);
//   otherBorders.forEach(removeBorder);
// });

// kDramasImage.addEventListener("click", () => {
//   showTrailer(kDramasTrailer, kdrama);

//   let otherTrailers = [
//     hollywoodTrailer,
//     bollywoodTrailer,
//     nollywoodTrailer,
//     tvSeriesTrailer,
//   ];
//   let otherBorders = [hollywood, bollywood, nollywood, tvSeries];

//   otherTrailers.forEach(removeTrailer);
//   otherBorders.forEach(removeBorder);
// });

// tvSeriesImage.addEventListener("click", () => {
//   showTrailer(tvSeriesTrailer, tvSeries);

//   let otherTrailers = [
//     hollywoodTrailer,
//     bollywoodTrailer,
//     nollywoodTrailer,
//     kDramasTrailer,
//   ];
//   let otherBorders = [hollywood, bollywood, nollywood, kdrama];

//   otherTrailers.forEach(removeTrailer);
//   otherBorders.forEach(removeBorder);
// });

// //function to show trailer and add border color
// function showTrailer(trailer, border) {
//   trailer.style.cssText = "display: block; animation:showTrailer 800ms ease";
//   border.classList.add("active");
// }
// //function to remove trailer
// function removeTrailer(trailer) {
//   trailer.style.display = "none";
// }
// //function to remove border
// function removeBorder(border) {
//   border.classList.remove("active");
// }
