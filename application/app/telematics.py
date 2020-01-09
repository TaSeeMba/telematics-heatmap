from app import app, utils
from flask import render_template, request
import csv
import os
import json

MAPS_API_KEY = os.environ.get('MAPS_API_KEY')

@app.route("/")
def index():
    return render_template("index.html", api_key=MAPS_API_KEY)

@app.route('/upload', methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':
        # Create variable for uploaded file
        request_file = request.files['file'] 
        request_file.save("myfile.csv") 
        if not request_file:
            return "No file"
        extractedPoints = utils.extract()
        if type(extractedPoints) != dict:
            return "Errors in data"
        result = utils.transform(extractedPoints)
        return json.dumps(result)
    else:
        return "Data upload failed!"
      
