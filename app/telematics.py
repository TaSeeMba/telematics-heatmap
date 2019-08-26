from app import app
from flask import render_template, request
import csv
import os

MAPS_API_KEY = os.environ.get('MAPS_API_KEY')

@app.route("/")
def index():
    print(MAPS_API_KEY)
    return render_template("index.html", api_key=MAPS_API_KEY)

@app.route('/upload', methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':
        # Create variable for uploaded file
        f = request.files['file']  

        #store the file contents as a string
        fstring = f.read()
        
        #create list of dictionaries keyed by header row
        # csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(fstring.splitlines(), skipinitialspace=True)]

        #do something list of dictionaries
        return fstring
    else:
        return "fail"
      
