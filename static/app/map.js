function geoFindMe() {
  function success(position) {
    var myLatitude = position.coords.latitude;
    var myLongitude = position.coords.longitude;
    const myLocation = { lat: myLatitude, lng: myLongitude };
    initMap(myLocation, true);
  }

  function error() {
    console.log("Unable to retrieve your position");
    // Provide a default center when geolocation fails
    const defaultLatLng = { lat: -1.202005, lng: 36.925171 };
    initMap(defaultLatLng, false);
  }

  if (!navigator.geolocation) {
    console.log("Geolocation is not supported by your browser");
    // Provide a default center when geolocation is not supported
    const defaultLatLng = { lat: -1.202005, lng: 36.925171 };
    initMap(defaultLatLng, false);
  } else {
    console.log("Locating…");
    navigator.geolocation.getCurrentPosition(success, error);
  }
}


function initMap(centerLatLng, showMarker) {
  const { Map, Marker } = google.maps;
  var options = {
    zoom: 15,
    center: centerLatLng,
  };
  const map = new Map(document.getElementById("map"), options);

  if (showMarker) {
    new Marker({
      position: centerLatLng,
      map,
    });
  }
}

// Call the initMap() function with the default center and hide the marker
const defaultLatLng = { lat: -1.202005, lng: 36.925171 };
initMap(defaultLatLng, false);


// Initialize the state variable
let useGeoLocation = false;

// Function to handle the button click
function toggleGeoLocation() {
  useGeoLocation = !useGeoLocation; // Toggle the state

  // Call the appropriate function based on the state
  if (useGeoLocation) {
    geoFindMe();
  } else {
    const defaultLatLng = { lat: -1.202005, lng: 36.925171 };
    initMap(defaultLatLng, false);
  }
}

// Add the event listener to the button
document.getElementById("find-me").addEventListener("click", toggleGeoLocation);