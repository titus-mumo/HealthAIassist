$(document).ready(function () {
  var theme = localStorage.getItem("theme");

  if (theme === "dark-mode") {
    $("#theme").addClass("dark-mode");
  }

  $("#theme").click(function () {
    $(this).toggleClass("dark-mode");
    var isDarkMode = $(this).hasClass("dark-mode");

    if (isDarkMode) {
      localStorage.setItem("theme", "dark-mode");
    } else {
      localStorage.setItem("theme", "light-mode");
    }
  });
});
