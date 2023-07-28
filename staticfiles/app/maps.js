function geoFindMe() {
  function success(position) {
    var myLatitude = position.coords.latitude;
    var myLongitude = position.coords.longitude;
    console.log("");
    console.log(myLatitude)
    console.log(myLongitude)
    const myLocation = {lat:myLatitude, lng:myLongitude}
  }

  function error() {
    console.log('unable to retrieve your position');
  }

  if (!navigator.geolocation) {
    console.log("Geolocation is not supported by your browser");
  } else {
    console.log("Locating…");
    navigator.geolocation.getCurrentPosition(success, error);
  }
}

document.getElementById("find-me").addEventListener("click", geoFindMe);

async function initMap() {
  const myLatLng = { lat: -1.202005, lng: 36.925171 };
  const { Map } = await google.maps.importLibrary("maps");
  var options = {
    zoom: 15,
    center: myLatLng,
  };
  const map = new Map(document.getElementById("map"), options);
  // new google.maps.Marker({
  //   position: myLatLng,
  //   map,
  // });
}

initMap();
document.getElementById('find-me').addEventListener("click", geoFindMe);
