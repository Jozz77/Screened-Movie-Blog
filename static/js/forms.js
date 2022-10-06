"use strict";

const resetInput1 = document.querySelector("#password-reset-1");
const resetInput2 = document.querySelector("#password-reset-2");
const eyeReset1 = document.querySelector("#eye-reset-1");
const eyeReset2 = document.querySelector("#eye-reset-2");
const form = document.querySelector(".form");
const errorMsg = document.querySelectorAll(".error-msg");

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

eyeReset1.addEventListener("click", () => {
  eyeReset1.classList.toggle("active");
  showPassword1();
});
eyeReset2.addEventListener("click", () => {
  eyeReset2.classList.toggle("active");
  showPassword2();
});

// password validation
form.addEventListener("submit", (e) => {
  e.preventDefault();
  checkPassword();
  checkInput();
});

function setError(errorMsg, inputName) {
  errorMsg.classList.add("active");
  inputName.style.border = "2px solid hsl(0, 100%, 74%)";
  inputName.style.outline = "none";
}

function checkInput() {
  const inputValue1 = resetInput1.value.trim();
  const inputValue2 = resetInput2.value.trim();

  if (inputValue1 !== inputValue2) {
    setError(errorMsg[1], resetInput2);
    errorMsg[1].textContent = "Password does not match";
  } else {
    errorMsg[1].classList.remove("active");
    resetInput2.style.border = "1px solid var(--text-color)";
  }
}

resetInput1.addEventListener("input", () => {
  console.log(resetInput1.value);
  if (resetInput1.value.length < 8) {
    errorMsg[0].textContent = "Cannot be less than 8 characters";
    setError(errorMsg[0], resetInput1);
  } else {
    errorMsg[0].classList.remove("active");
    resetInput1.style.border = "1px solid var(--text-color)";
  }
});

function checkPassword() {}

// document.addEventListener('')
