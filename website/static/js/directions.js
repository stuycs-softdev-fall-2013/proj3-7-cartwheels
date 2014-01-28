var calcRoute;
var initialize;
var codeAddress;

var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
var map;
var geocoder;

var slat, slng, elat, elng;
var start, end;
var mode_id;

var create_map = function (sAddress, eAddress, map_id, directions_id, id_mode) {
    "use strict";

    mode_id = id_mode;

    initialize = function() {
        geocoder = new google.maps.Geocoder();

        directionsDisplay = new google.maps.DirectionsRenderer();

        var mapOptions = {
            zoom: 18,
            center: new google.maps.LatLng(40.717975, -74.014037)
        };

        map = new google.maps.Map(document.getElementById(map_id), mapOptions);
        directionsDisplay.setMap(map);
        directionsDisplay.setPanel(document.getElementById(directions_id));
        codeAddress();
    };

    codeAddress = function () {
        geocoder.geocode({ 'address': sAddress},
            function (results, status) {
                if (status === google.maps.GeocoderStatus.OK) {
                    start = results[0].geometry.location;
                    map.setCenter(results[0].geometry.location);
                } else {
                    alert("Geocode was not successful because: " + status);
                }
            });

        end = eAddress;
    };

    calcRoute = function () {

        var selectedMode = document.getElementById(mode_id).value;

        var request = {
            origin: start,
            destination: end,
            travelMode: google.maps.TravelMode[selectedMode]
        };
        directionsService.route(request, function (response, status) {
            if (status === google.maps.DirectionsStatus.OK) {
                directionsDisplay.setDirections(response);
            } else {
                alert("error displaying directions");
            }
        });
    };

    google.maps.event.addDomListener(window, 'load', initialize);
}
