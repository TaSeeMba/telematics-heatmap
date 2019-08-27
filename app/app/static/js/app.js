// This example requires the Visualization library. Include the libraries=visualization
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">

var map, heatmap;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 13,
    center: {lat: 37.775, lng: -122.434},
    mapTypeId: 'satellite',
  });

  heatmap = new google.maps.visualization.HeatmapLayer({
    data: new Utilities().getSamplePoints(),
    map: map
  });
}

function loadMap(mapPoints) {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: {lat: mapPoints.userCentreLocation.lat, lng: mapPoints.userCentreLocation.lon},
    mapTypeId: 'satellite'
  });

  heatmap = new google.maps.visualization.HeatmapLayer({
    data: mapPoints.points,
    map: map
  });
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
  heatmap.set('radius', heatmap.get('radius') ? null : 20);
}

function changeOpacity() {
  heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}

function submitCsvForm() {
  console.log("submit event");
  var fd = new FormData(document.getElementById("fileinfo"));
  console.log(fd);
}

function getPointsFromCSV(jsonData) {
  var points = [];
  var maxWeight = 0; 
  let centreLoc = new UserLocation(0, 0);
  for (var i = 0; i < jsonData.length; i++) {
    var data = jsonData[i];
    points.push({location: new google.maps.LatLng(parseFloat(data[0]), parseFloat(data[1])), weight: parseInt(data[2])} );
    if (maxWeight < data[2]) {
      centreLoc.lat = parseFloat(data[0]);
      centreLoc.lon = parseFloat(data[1]);
      weight = data[2];
    }
  }
  return new MapPoints(centreLoc, points);
}

$(document).ready(function() { 
  console.log("ENTERED");
  $("#button_upload").click(function() { 
    var fd = new FormData(); 
    var files = $('#file')[0].files[0]; 
    fd.append('file', files); 
    $.ajax({ 
        url: '/upload', 
        type: 'post', 
        data: fd, 
        contentType: false, 
        processData: false, 
        success: function(response){ 
            console.log(response);
            if(response != 0){ 
              var jsonData = JSON.parse(response);
              var mapPoints = getPointsFromCSV(jsonData);
              loadMap(mapPoints);
              alert('CSV successfully uploaded and processed. Click OK for visualization.'); 
            } 
            else{ 
                alert('Something went wrong. Please check your data and try again.'); 
            } 
        }, 
    }); 
  }); 
});