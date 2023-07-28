const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const dropdown = document.getElementById("dropdownMenu");

searchInput.addEventListener("input", function () {
  const searchValue = searchInput.value.trim().toLowerCase();

  if (searchValue.length > 0) {
    searchButton.removeAttribute("disabled");
  } else {
    searchButton.setAttribute("disabled", "true");
  }
});

dropdown.addEventListener("change", function () {
  const selectedValue = dropdown.value;
  searchInput.value = selectedValue;

  if (selectedValue.length > 0) {
    searchButton.removeAttribute("disabled");
  } else {
    searchButton.setAttribute("disabled", "true");
  }
});

fetch("/app/search_doctor")
  .then((response) => response.json())
  .then((data) => {
    // Clear existing options
    dropdown.innerHTML = "";

    // Process the data received from the server
    data.forEach((name) => {
      // Create an option element for each name
      const option = document.createElement("option");
      option.text = name;
      option.value = name;

      // Append the option to the dropdown
      dropdown.appendChild(option);
    });

    // Update search input on dropdown option change
    dropdown.addEventListener("change", function () {
      searchInput.value = dropdown.value;
    });
  })
  .catch((error) => {
    // Handle any errors that occur during the request
    console.error("Error:", error);
  });
