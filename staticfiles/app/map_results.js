async function initMap() {
  const myLatLng = { lat: -1.1958929893863986, lng: 36.926161801736676 };
  const kuLatLng = { lat: latitude, lng: longitude };
  const { Map } = await google.maps.importLibrary("maps");
  var options = {
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
    travelMode: google.maps.TravelMode.DRIVING,
  };

  directionsService.route(request, function (result, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      directionsRenderer.setDirections(result);
    }
  });
}

initMap();
