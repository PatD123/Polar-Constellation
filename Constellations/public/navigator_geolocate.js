if("geolocation" in navigator){
    console.log("You can use geolocator!");
    navigator.geolocation.getCurrentPosition((position) => {
        const lat = position.coords.latitude;
        const long = position.coords.longitude;
    });
}
