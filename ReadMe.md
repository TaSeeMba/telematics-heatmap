# Telematics HeatMap (Still under development)
This project is intended to be a visualization library for telematics data. Upload a CSV that contains fields `lat` and `lon` (case insenstive) and this application will render a heat map visualization of your data points. 

This app also comes with the following functionality:
- Toggling heatmap on and off
- Changing gradient of heatmap visualization
- Changing radius of heatmap visualization
- Changing opacity of heatmap visualization

# Preview of Running Application

![Image description](sample.png)

# Getting Started

Get a Google Maps API key. Instructions are here: https://developers.google.com/maps/documentation/javascript/get-api-key .

* Ensure that you are running in a Python 3 environment.

# Running Application in  Locally
1. Setup virtual environment
```
python3 -m venv env
source ./env/bin/activate
python -m pip install package
```

2. Setup the `MAPS_API_KEY` inside your virtual environment :
`export MAPS_API_KEY=<MAPS_API_KEY_FROM_GOOGLE>`

3. Install application dependencies
`pip install --no-cache-dir -r requirements.txt`

4. Run application:
`python main.py`

5. Open the front-end web application: 
In your web browser, navigate to the address `http://127.0.0.1:5000/` and upload a CSV file with your telematics data. 

# Running Application in  Docker

To build application : `docker build -t heatmapimage .`

To run application: 

`docker run -d --name heatmaps -e MAPS_API_KEY=<MAPS_API_KEY_FROM_GOOGLE> -p 80:80 heatmapimage`

You should be able to check it in your Docker container's URL, for example: http://192.168.99.100 or http://127.0.0.1

