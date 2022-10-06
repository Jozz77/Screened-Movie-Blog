const resetInput1 = document.querySelector("#password-reset-1");
const resetInput2 = document.querySelector("#password-reset-2");

const eyeReset1 = document.querySelector("#eye-reset-1");
const eyeReset2 = document.querySelector("#eye-reset-2");

function showPassword1() {
  if (resetInput1.type === "password") {
    resetInput1.type = "text";
  } else {
    resetInput1.type = "password";
  }
}
function showPassword2() {
  if (resetInput2.type === "password") {
    resetInput2.type = "text";
  } else {
    resetInput2.type = "password";
  }
}

eyeReset1.addEventListener("click", showPassword1);
eyeReset2.addEventListener("click", showPassword2);
