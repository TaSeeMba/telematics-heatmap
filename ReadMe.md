# Telematics HeatMap
This project is intended to be a visualization library for telematics data. Upload a CSV that contains fields `lat` and `lon` (case insenstive) and this application will render a heat map visualization of your data points. 

This app also comes with the following functionality
- Toggling heatmap on and off
- Changing gradient of heatmap visualization
- Changing radius of heatmap visualization
- Changing opacity of heatmap visualization

# Preview of Running Application

![Image description](sample.png)

# Getting Started

Get a Google Maps API key. Instructions are here: `https://developers.google.com/maps/documentation/javascript/get-api-key#restrict_key`

# Running Application 

To build application : `docker build -t myimage .`

To run application: `docker run -d --name mycontainer -p 80:80 myimage`

You should be able to check it in your Docker container's URL, for example: http://192.168.99.100 or http://127.0.0.1

