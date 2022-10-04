//getting the elements through DOM
const hollywoodImage = document.querySelector("#hollywood-img");
const hollywoodTrailer = document.querySelector("#hollywood-trailer");
const hollywood = document.querySelector("#hollywood");

const bollywoodImage = document.querySelector("#bollywood-img");
const bollywoodTrailer = document.querySelector("#bollywood-trailer");
const bollywood = document.querySelector("#bollywood");

const nollywoodImage = document.querySelector("#nollywood-img");
const nollywoodTrailer = document.querySelector("#nollywood-trailer");
const nollywood = document.querySelector("#nollywood");

const kDramasImage = document.querySelector("#kdramas-img");
const kDramasTrailer = document.querySelector("#kdrama-trailer");
const kdrama = document.querySelector("#k-dramas");

const tvSeriesImage = document.querySelector("#tvseries-img");
const tvSeriesTrailer = document.querySelector("#tvseries-trailer");
const tvSeries = document.querySelector("#tv-series");

/*added a click event listener to the images to make the trailer 
box show when the image is clicked;
made sure other boxes weren't visible when the active one is and
removed the active class on the borders of inactive images
*/
hollywoodImage.addEventListener("click", () => {
  showTrailer(hollywoodTrailer, hollywood);

  let otherTrailers = [tvSeriesTrailer, bollywoodTrailer, nollywoodTrailer, kDramasTrailer];
  let otherBorders = [tvSeries, bollywood, nollywood, kdrama];

  otherTrailers.forEach(removeTrailer);
  otherBorders.forEach(removeBorder);
});


bollywoodImage.addEventListener("click", () => {
  showTrailer(bollywoodTrailer, bollywood);

  let otherTrailers = [hollywoodTrailer, tvSeriesTrailer, nollywoodTrailer, kDramasTrailer,];
  let otherBorders = [hollywood, tvSeries, nollywood, kdrama];

  otherTrailers.forEach(removeTrailer);
  otherBorders.forEach(removeBorder);
});


nollywoodImage.addEventListener("click", () => {
  showTrailer(nollywoodTrailer, nollywood);

  let otherTrailers = [hollywoodTrailer, bollywoodTrailer, tvSeriesTrailer, kDramasTrailer,];
  let otherBorders = [hollywood, bollywood, kdrama, tvSeries];

  otherTrailers.forEach(removeTrailer);
  otherBorders.forEach(removeBorder);
});

kDramasImage.addEventListener("click", () => {
  showTrailer(kDramasTrailer, kdrama);

  let otherTrailers = [hollywoodTrailer, bollywoodTrailer, nollywoodTrailer, tvSeriesTrailer];
  let otherBorders = [hollywood, bollywood, nollywood, tvSeries];

  otherTrailers.forEach(removeTrailer);
  otherBorders.forEach(removeBorder);
});

tvSeriesImage.addEventListener("click", () => {
  showTrailer(tvSeriesTrailer, tvSeries);

  let otherTrailers =[hollywoodTrailer, bollywoodTrailer, nollywoodTrailer, kDramasTrailer];
  let otherBorders = [hollywood, bollywood, nollywood,kdrama];

  otherTrailers.forEach(removeTrailer);
  otherBorders.forEach(removeBorder);
});

//function to show trailer and add border color
function showTrailer(trailer, border) {
  trailer.style.cssText = "display: block; animation:showTrailer 800ms ease";
  border.classList.add("active");
}
//function to remove trailer
function removeTrailer(trailer){
  trailer.style.display = "none";
}
//function to remove border
function removeBorder(border){
  border.classList.remove("active");
}