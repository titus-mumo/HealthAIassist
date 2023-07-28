document.addEventListener("DOMContentLoaded", function () {
  // Get the theme element
  var themeDiv = document.getElementById("theme");
  // Get the body element
  var body = document.body;

  // Add a click event listener to the theme-div
  themeDiv.addEventListener("click", function () {
    // Toggle the theme by adding/removing the 'dark-theme' class from the body
    body.classList.toggle("dark-theme");
    // Toggle the theme by adding/removing the 'light-theme' class from the body
    body.classList.toggle("light-theme");
  });
});
