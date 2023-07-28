async function initMap(travelMode) {
  const myLatLng = { lat: -1.1958929893863986, lng: 36.926161801736676 };
  const kuLatLng = { lat: latitude, lng: longitude };
  const { Map } = await google.maps.importLibrary("maps");
  const options = {
    zoom: 15,
    center: myLatLng,
  };
  const map = new Map(document.getElementById("map"), options);
  const directionsService = new google.maps.DirectionsService();
  const directionsRenderer = new google.maps.DirectionsRenderer({
    map,
  });

  const request = {
    origin: myLatLng,
    destination: kuLatLng,
    travelMode: google.maps.TravelMode[travelMode.toUpperCase()],
  };

  directionsService.route(request, function (result, status) {
    if (status === google.maps.DirectionsStatus.OK) {
      directionsRenderer.setDirections(result);

      // Add labels to the markers with custom CSS styling
      const route = result.routes[0];
      const distance = route.legs[0].distance.text;
      console.log("Distance:", distance)
      document.getElementById("distance").textContent = distance;
      for (let i = 0; i < route.legs.length; i++) {
        const leg = route.legs[i];
        const startMarker = new google.maps.Marker({
          position: leg.start_location,
          label: {
            text: "My Location", // Label for the starting point marker
            fontWeight: "bold", // Apply bold font weight
            fontSize: "18px", // Increase font size
          },
          map: map,
        });
        const endMarker = new google.maps.Marker({
          position: leg.end_location,
          label: {
            text: "Doctor's Location", // Label for the destination marker
            fontWeight: "bold", // Apply bold font weight
            fontSize: "18px", // Increase font size
          },
          map: map,
        });
      }
    }
  });
}

// Call the initMap function with the default travel mode
initMap("driving");

// Function to handle the mode change
function changeTravelMode() {
  const selectedMode = document.getElementById("mode-select").value;
  initMap(selectedMode);
}

// Add event listener to the mode select element
document
  .getElementById("mode-select")
  .addEventListener("change", changeTravelMode);
