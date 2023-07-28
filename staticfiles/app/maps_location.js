async function initMap() {
    const DoctorLatLng = { lat: latitude, lng: longitude };
    const { Map } = await google.maps.importLibrary("maps");
    var options = {
        zoom: 15,
        center: DoctorLatLng,
        };

    const map = new Map(document.getElementById("map"), options);
    new google.maps.Marker({
        position: DoctorLatLng,
        map,
    });
}


initMap();
