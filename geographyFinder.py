'''
Dependencies:
    *Self built methods*
    -NONE
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
|       - DART ADD YOUR GITHUB USERNAME              |
|----------------------------------------------------|
'''
import json
import requests
from shapely.geometry import shape, Point
import csv
import os

def getWard(lon,lat,map_from):
    if map_from.lower() == 'local': #If loading geoJson from local file
        wardGeoJson_filename = '.'+ os.path.sep+'GeoJson'+ os.path.sep+'Ward_2012.geojson'
        with open(wardGeoJson_filename) as f: # load GeoJSON file containing sectors
            geo_json_data = json.load(f)

    elif map_from.lower() == 'api':
        # Call dc open data API for 2012 ward geoJson file
        geo_json_raw = requests.get('https://opendata.arcgis.com/datasets/0ef47379cbae44e88267c01eaec2ff6e_31.geojson')  #This should be the 2012 ward map from DC Open Gov
        geo_json_data = geo_json_raw.json()

    point = Point(lon, lat) # construct point based on lon/lat returned by geocoder
    ward_value = '!!PRE-FOUND!!'

    for feature in geo_json_data['features']: # check each polygon to see if it contains the point
        polygon = shape(feature['geometry'])
        try:        #FIXME I may not need the try/except anymore.  Keep around for a few iterations to double check.
            if polygon.contains(point):
                ward_value = feature['properties']['WARD_ID']
                break
            else: ward_value = '!!NOTFOUND--TRY!!'
        except:
            ward_value = '!!NOTFOUND--EXCEPT!!'
    return(ward_value)
    
### Possible other GET methods
def getNeighborhood(lon,lat,map_from):
    return('NONE')
def getTract(lon,lat,map_from):
    return('NONE')
def getQuandrant(lon,lat,map_from):
    return('NONE')
def getANC(lon,lat,map_from):
    return('NONE')
'''  *****************        APPENDICES   *************************
                    I.Changes to look into or needed
1) [IMPLEMENTED NOT TESTED]
    - Use OS to get current working directory and add in the GeoJson folder for any user
2) Create a file of methods rather than one time use script
                    II.
                    III.
                    IV.
*****************        END APPENDICES   *************************'''
