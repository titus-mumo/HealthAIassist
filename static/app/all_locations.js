async function initMap() {
  const doctorLocations = doctor_locations ;
  const { Map, Marker } = await google.maps.importLibrary("maps");

  const mapOptions = {
    zoom: 10,
    center: new google.maps.LatLng(-1.1958929893863986, 36.926161801736676),
  };

  const map = new Map(document.getElementById("map"), mapOptions);

  doctorLocations.forEach(function (doctor) {
    const marker = new Marker({
      position: new google.maps.LatLng(doctor.latitude, doctor.longitude),
      map: map,
    });
  });
}

initMap();