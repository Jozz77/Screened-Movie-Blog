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

  bollywoodTrailer.style.display = "none";
  bollywood.classList.remove("active");

  nollywoodTrailer.style.display = "none";
  nollywood.classList.remove("active");

  kDramasTrailer.style.display = "none";
  kdrama.classList.remove("active");

  tvSeriesTrailer.style.display = "none";
  tvSeries.classList.remove("active");
});
bollywoodImage.addEventListener("click", () => {
  showTrailer(bollywoodTrailer, bollywood);

  hollywoodTrailer.style.display = "none";
  hollywood.classList.remove("active");

  nollywoodTrailer.style.display = "none";
  nollywood.classList.remove("active");

  kDramasTrailer.style.display = "none";
  kdrama.classList.remove("active");

  tvSeriesTrailer.style.display = "none";
  tvSeries.classList.remove("active");
});
nollywoodImage.addEventListener("click", () => {
  showTrailer(nollywoodTrailer, nollywood);

  hollywoodTrailer.style.display = "none";
  hollywood.classList.remove("active");

  bollywoodTrailer.style.display = "none";
  bollywood.classList.remove("active");

  kDramasTrailer.style.display = "none";
  kdrama.classList.remove("active");

  tvSeriesTrailer.style.display = "none";
  tvSeries.classList.remove("active");
});
kDramasImage.addEventListener("click", () => {
  showTrailer(kDramasTrailer, kdrama);

  hollywoodTrailer.style.display = "none";
  hollywood.classList.remove("active");

  nollywoodTrailer.style.display = "none";
  nollywood.classList.remove("active");

  bollywoodTrailer.style.display = "none";
  bollywood.classList.remove("active");

  tvSeriesTrailer.style.display = "none";
  tvSeries.classList.remove("active");
});
tvSeriesImage.addEventListener("click", () => {
  showTrailer(tvSeriesTrailer, tvSeries);

  hollywoodTrailer.style.display = "none";
  hollywood.classList.remove("active");

  bollywoodTrailer.style.display = "none";
  bollywood.classList.remove("active");

  nollywoodTrailer.style.display = "none";
  nollywood.classList.remove("active");

  kDramasTrailer.style.display = "none";
  kdrama.classList.remove("active");
});

//function to show trailer and add border color
function showTrailer(trailer, border) {
  trailer.style.cssText = "display:block; animation:showTrailer 800ms ease";
  border.classList.add("active");
}
