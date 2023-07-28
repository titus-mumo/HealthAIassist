document.addEventListener("DOMContentLoaded", function () {
  // Get the theme element
  var themeDiv = document.getElementById("theme");
  var pElement = document.getElementById("theme-p");
  // Get the body element
  var body = document.body;
  body.style.visibility = 'visible';

  // Check for existing theme preference
  var themePreference = localStorage.getItem("theme");
  if (themePreference) {
    // Apply the stored theme preference
    body.classList.add(themePreference);
    pElement.textContent =
      themePreference === "dark-theme" ? "Dark Mode" : "Light Mode";
  }

  // Add a click event listener to the theme-div
  themeDiv.addEventListener("click", function () {
    // Toggle the body class for dark and light theme
    body.classList.toggle("dark-theme");
    body.classList.toggle("light-theme");

    // Toggle the text content of the p element
    if (body.classList.contains("dark-theme")) {
      pElement.textContent = "Dark Mode";
      body.style.visibility = 'visible';
      // Store the theme preference in local storage
      localStorage.setItem("theme", "dark-theme");
    } else {
      pElement.textContent = "Light Mode";
      // Store the theme preference in local storage
      localStorage.setItem("theme", "light-theme");
      body.style.visibility = "visible";
    }
  });
});
