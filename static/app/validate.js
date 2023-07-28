// Get the button element and input container element
var button = document.querySelector(".btn-info");
var inputContainer = document.getElementById("inputContainer");
var inputField = document.getElementById("inputField");

// Function to toggle the visibility of the input container, update the button text, and set focus to the input field with the cursor at the beginning
function showInputField() {
  if (inputContainer.style.display === "none") {
    inputContainer.style.display = "block";
    button.innerHTML =
      '<i class="fa-sharp fa-solid fa-minus"></i> Close Input Field';
    inputField.style.display = "block";
    inputField.style.textAlign = "top"; // Set text alignment to left
    inputField.focus();
    inputField.setSelectionRange(0, 0);
  } else {
    inputContainer.style.display = "none";
    button.innerHTML =
      '<i class="fa-sharp fa-solid fa-plus"></i> Add Input Field';
  }
}

// Attach the showInputField function to the button's click event
button.addEventListener("click", showInputField);

function toggleButtonClass(button) {
  var yesButton = button.parentNode.querySelector('[value="yes"]');
  var noButton = button.parentNode.querySelector('[value="no"]');
  var inputField = button.parentNode.querySelector('input[type="hidden"]');

  if (button.value === "yes") {
    if (button.classList.contains("btn-primary")) {
      button.classList.remove("btn-primary");
      button.classList.add("btn-outline-primary");
    } else {
      button.classList.remove("btn-outline-primary");
      button.classList.add("btn-primary");
      noButton.classList.remove("btn-primary");
      noButton.classList.add("btn-outline-primary");
    }
  } else if (button.value === "no") {
    if (button.classList.contains("btn-primary")) {
      button.classList.remove("btn-primary");
      button.classList.add("btn-outline-primary");
    } else {
      button.classList.remove("btn-outline-primary");
      button.classList.add("btn-primary");
      yesButton.classList.remove("btn-primary");
      yesButton.classList.add("btn-outline-primary");
    }
  }
  if (button.classList.contains("btn-primary")) {
    inputField.value = button.value;
  } else {
    inputField.value = "";
  }
}

function validateForm() {
  var signs = document.getElementsByClassName("prompt-container");

  for (var i = 0; i < signs.length; i++) {
    var yesButton = signs[i].querySelector('button[value="yes"]');
    var noButton = signs[i].querySelector('button[value="no"]');

    if (
      !yesButton.classList.contains("btn-primary") &&
      !noButton.classList.contains("btn-primary")
    ) {
      document.getElementById("message").textContent =
        "Please make sure to fill the entire form";
      return false;
    }
  }

  return true; // Allow form submission
}

const storedColor = localStorage.getItem("backgroundColor");

if (storedColor) {
  document.getElementByClass("side-bar-value").style.backgroundColor =
    storedColor;
}

function updateColor(color) {
  document.getElementByClaa("side-bar-value").style.backgroundColor = color;
  localStorage.setItem("backgroundColor", color);
}

function clearStoredColor() {
  document.getElementByClass("side-bar-value").style.backgroundColor = "";
  localStorage.removeItem("backgroundColor");
}
