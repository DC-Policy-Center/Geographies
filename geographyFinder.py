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

def getWard(lon,lat,map_from):

    if map_from.lower() == 'local':
        #If loading geoJson from local file
        try:
            wardGeoJson_filename = './/GeoJson//Ward_2012.geojson'
        except:
            wardGeoJson_filename = '.\\GeoJson\\Ward_2012.geojson'
        # load GeoJSON file containing sectors
        with open(wardGeoJson_filename) as f:
            geo_json_data = json.load(f)
    elif map_from.lower() == 'api':
# Call dc open data API for 2012 ward geoJson file
        geo_json_raw = requests.get('https://opendata.arcgis.com/datasets/0ef47379cbae44e88267c01eaec2ff6e_31.geojson')  #This should be the 2012 ward map from DC Open Gov
        geo_json_data = geo_json_raw.json()
        # construct point based on lon/lat returned by geocoder
    point = Point(lon, lat)

    # check each polygon to see if it contains the point
    for feature in geo_json_data['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            try:
                ward_value = feature['properties']['WARD_ID']
            except:
                ward_value = '!!NOTFOUND!!'
    return(ward_value)

'''  *****************        APPENDICES   *************************
                    I.Changes to look into or needed
1) Use OS to get current working directory and add in the GeoJson folder for any user
2) Create a file of methods rather than one time use script
                    II.
                    III.
                    IV.
*****************        END APPENDICES   *************************'''
