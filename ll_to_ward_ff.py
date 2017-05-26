'''
Dependencies:
    *Self built methods*
    -geographyFinder
    *Libraries*
    - json
    - requests
    - shapely
    - csv
This is an early version of mapping addresses to different geographies,
starting with DC Wards

|Signature-------------------------------------------|
|Written for DC Policy Center by                     |
|Michael Watson & Dart Howell; 2017                  |
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:                                             |
|       - M-Watson & MW-DC-Policy-Center             |
|       - darthowell                                 |
|----------------------------------------------------|
'''
import json
import requests
from shapely.geometry import shape, Point
import geocoder
import csv
import geographyFinder

data = []
sales_file = 'hidden_output_lat_lng.csv'  # Change to your absolute location for reading in sales file
with open(sales_file) as csvfile:
    data_reader = csv.reader(csvfile)
    for row in data_reader:
        data.append(row)


full_address_index = data[0].index('Full Address')

# Find the column number that lat/lon values are located
lat_index = data[0].index('lat')
lon_index = data[0].index('lon')

for i in range(len(data)):
    if i != 0:
        lat =  float(data[i][lat_index])
        lon =  float(data[i][lon_index])

        if i%50 == 0:
            print('still moving  '+str(i)+' out of: '+str(len(data)))
            #################################################
        ward_value = geographyFinder.getWard(lon,lat,'local')
        try:
            data[i].append(ward_value)
        except:
            print('failed ward value at index:  %i'%(i))
            data[i].append('-1')


# Write results to an output CSV file
with open('hidden_output.csv','w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow(row)

'''  *****************        APPENDICES   *************************
                    I.Changes to look into or needed
1) Use OS to get current working directory and add in the GeoJson folder for any user
2) Create a file of methods rather than one time use script
                    II.
                    III.
                    IV.
*****************        END APPENDICES   *************************'''
