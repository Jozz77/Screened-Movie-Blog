"use strict";

const eyeIcon = document.querySelectorAll(".password-icon");
const formInput = document.querySelectorAll(".form__input");
const formInputActive = document.querySelectorAll(".input-active");
const eyeIconActive = document.querySelectorAll(".icon-active");
let eyeNum = 0;
let inputNum = 0;
let state = false;

formInput.forEach((input, idx) => {
  input.addEventListener("mouseenter", () => {
    inputNum = idx;
    updateInputField();
    updateEyeIcon();
  });
});

eyeIcon.forEach((icon, idx) => {
  icon.addEventListener("mouseenter", () => {
    eyeNum = idx;
    updateInputField();
    updateEyeIcon();
  });
});

eyeIconActive.forEach((icon) => {
  icon.addEventListener("click", () => {
    showPassword();
  });
});

// getting indexes of icons and input elements
// eyeIcon.forEach((icon, idx) => {
//   idx = inputNum;
//   eyeNum = idx;
// });

// eyeIcon[eyeNum].addEventListener("click", showPassword);

// function showPassword() {
//   console.log(inputNum);
//   if (formInput[inputNum].type === "password") {
//     formInput[inputNum].type = "text";
//     console.log(formInput[inputNum].type);
//   } else {
//     formInput[inputNum].type = "password";
//   }
// }

// const formInputActive = document.querySelectorAll(".input-active");

function updateInputField() {
  formInput.forEach((input) => {
    if (input.classList.contains("input-active")) {
      input.classList.remove("input-active");
    }
  });
  formInput[inputNum].classList.add("input-active");
}

function updateEyeIcon() {
  eyeIcon.forEach((icon) => {
    if (icon.classList.contains("icon-active")) {
      icon.classList.remove("icon-active");
    }
  });

  eyeIcon[eyeNum].classList.add("icon-active");
}

function showPassword() {
  formInputActive.forEach((input) => {
    console.log(input);
    if (input.type === "password") {
      input.type = "text";
      // console.log(input.type);
    } else {
      input.type = "password";
    }
  });
}

// function hidePassword() {
//   formInput.forEach((input) => {
//     input.type = "password";
//   });
// }

// eyeIcon.forEach((icon) => {
//   console.log("hello");
// });
