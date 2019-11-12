import requests
#This uses the https://developer.here.com/ api for geocoding

#Put in your HERE keys they provide after you sign up
APP_ID = 'APP_ID HERE'
APP_CODE = 'APP_CODE HERE'


#How frequently to print the progress text
progress_check_interval = 100

#Variable initialization
address_index = 0
address_len = len(address_list)
found_latlon = []
not_found_latlon = []




#Use this list as your full data set. If you need a different format, tweek how the request is built
address_list = ["1310 L St. NW Washington D.C."]




for address in address_list:
    if address_index % 100: print("\nrequesting {} of {}\n".format(address_index,address_len)
    url = "https://geocoder.api.here.com/6.2/geocode.json?app_id={}&app_code={}&searchtext={}".format(APP_ID,APP_CODE,address)
    address_data = requests.get(url)
    address_json = address_data.json()
    try:
        lat_lon = address_json["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
        found_latlon.append(latlon)
    except:
        not_found_latlon.append(address)
