from app import app
from flask import render_template, request
import csv
import os
import json

MAPS_API_KEY = os.environ.get('MAPS_API_KEY')

@app.route("/")
def index():
    return render_template("index.html", api_key=MAPS_API_KEY)

'''
# This function primarily extracts lat and long data from any CSV file with columns contains case insensitive characters 'lat' and 'lon'
# The function reads the uploaded CSV, then looks for lat and lon columns before creating a data structure of the extracted data. 
# Data read from the CSV is converted into a dictionary with the following structure : <K:V> --> { (lat, lon) : weight } where the dictionary key is a tupple of lat and lon values.
# This data structure allows for creation of weighted data points for faster rendering of maps and emphasis analysis to your data.
'''
def extract():
    with open('myfile.csv') as f:
        reader = csv.reader(f, delimiter=',')
        line_count = 0
        latIndex = 0
        lonIndex = 0
        my_dictionary = {}
        for row in reader:
            if line_count == 0:
                for i, j in enumerate(row):
                    if j.__contains__('lat'):
                        latIndex = i
                    elif j.__contains__('lon'):
                        lonIndex = i
                if latIndex == 0 and lonIndex == 0:
                    return 'Incorrect format of CSV'
                line_count += 1
            else:
                lat = row[latIndex]
                lon = row[lonIndex]
                if (lat,lon) in my_dictionary.keys():
                    # retrieve current weight of gps location
                    oldWeight = my_dictionary.get((lat,lon))
                    newWeight = oldWeight + 1
                    # update weight
                    my_dictionary[(lat,lon)] = newWeight
                else:
                    my_dictionary.update({(lat,lon) : 1})
                line_count += 1
    f.close()
    os.remove('myfile.csv')
    return my_dictionary

'''
Transforms the extracted telematics data into a refined List with data structured as [lat, lon, weight] value. 
'''
def transform(data):
    return [ [*k,v] for k, v in data.items() ]

@app.route('/upload', methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':
        # Create variable for uploaded file
        request_file = request.files['file'] 
        request_file.save("myfile.csv") 
        if not request_file:
            return "No file"
        extractedPoints = extract()
        if type(extractedPoints) != dict:
            return "Errors in data"
        result = transform(extractedPoints)
        return json.dumps(result)
    else:
        return "Data upload failed!"
      
