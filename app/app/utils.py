import csv
import os
import logging

'''
Evaluates whether a given data point is not an empty string, a None value or a 0.0 gps co-ordinate.
'''
def isValidDataPoint(point):
    return bool(point and point.strip()) and float(point) != 0.0

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
                try :
                    lat = row[latIndex]
                    lon = row[lonIndex]
                    # coordinates of value 0.0 and None is bad data - skip them
                    if (isValidDataPoint(lat) and isValidDataPoint(lon)): 
                        if (lat,lon) in my_dictionary.keys():
                            # retrieve current weight of gps location
                            oldWeight = my_dictionary.get((lat,lon))
                            newWeight = oldWeight + 1
                            # update weight
                            my_dictionary[(lat,lon)] = newWeight
                        else:
                            my_dictionary.update({(lat,lon) : 1})
                except :
                    logging.exception("Ignoring bad data point.")
                line_count += 1
    f.close()
    os.remove('myfile.csv')
    return my_dictionary

'''
Transforms the extracted telematics data into a refined List with data structured as [lat, lon, weight] value. 
'''
def transform(data):
    return [ [*k,v] for k, v in data.items() ]