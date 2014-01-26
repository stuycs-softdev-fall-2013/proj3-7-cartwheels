    
      var directionsDisplay;
      var directionsService = new google.maps.DirectionsService();
      var map;
      var geocoder;

      var sAddress = "{{saddress}}";
      var eAddress = "{{eaddress}}";

      var slat, slng, elat, elng;
      var start, end;


      function initialize() {
      geocoder = new google.maps.Geocoder();

      directionsDisplay = new google.maps.DirectionsRenderer();

      

      var mapOptions = {
      zoom: 18,
      center: new google.maps.LatLng(40.717975, -74.014037)
      }
      map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
      directionsDisplay.setMap(map);
      directionsDisplay.setPanel(document.getElementById('directions-panel'));
      codeAddress();
      
      }

      function codeAddress() {

      geocoder.geocode( { 'address': sAddress}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
      start = results[0].geometry.location;
      map.setCenter(results[0].geometry.location);
      }
      else {
      alert("Geocode was not successful because: " + status);
      }
      });
      

      geocoder.geocode( { 'address': eAddress}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
      end = results[0].geometry.location;
      }
      else {
      alert("Geocode was not successful because: " + status);
      }
      });
      
      }

      function calcRoute() {
      var selectedMode = document.getElementById('mode').value;
      var request = {
      origin: start,
      destination: end,
      travelMode: google.maps.TravelMode[selectedMode]
      };
      directionsService.route(request, function(response, status) {
      if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
      }
      });
      }

      google.maps.event.addDomListener(window, 'load', initialize);



