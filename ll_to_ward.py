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
import csv
import geographyFinder

data = []
sales_file = '2016_sales_20011.csv'  # Change to your absolute location for reading in sales file
with open(sales_file) as csvfile:
    data_reader = csv.reader(csvfile)
    for row in data_reader:
        data.append(row)
data[0].append('city')
data[0].append('lat')
data[0].append('lon')
data[0].append('ward')



for i in range(len(data)):
    if i != 0:
        data[i].append('Washington, DC')

        ##### This is the LAT LONG LOOKUP WOULD GO



        #####
        #### FOR TESTING, ALL SHOULD BE IN 6th Ward.
        data[i].append(38.885288)
        data[i].append(-76.993688)

# Find the column number that lat/lon values are located
lat_index = data[0].index('lat')
lon_index = data[0].index('lon')

for i in range(len(data)):
    if i != 0:
        lat =  data[i][lat_index]
        lon =  data[i][lon_index]
        if i%30 == 0:
            print('still moving  '+str(i)+' out of: '+str(len(data)))
        ward_value = geographyFinder.getWard(lon,lat,'local')

        data[i].append(ward_value)


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
