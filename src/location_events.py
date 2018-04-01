import requests
import json
from urllib2 import urlopen

PRINT_DEBUG_LOGS=1

def debug_log(str):
    if PRINT_DEBUG_LOGS:
        print(str)

def location_details(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    #debug_log(j['results'])
    components = j['results'][0]['address_components']
    place_id = j['results'][0]['place_id'] #Use this for getting cities nearby
   # debug_log(components)
    country = town = None
    for c in components:
        if "locality" in c['types']:
            city = c['long_name']
        if "country" in c['types']:
            country = c['long_name']
    debug_log(city+":"+place_id)
    return city, country

def get_coordinates():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    return lat,lon

if __name__ == '__main__':
    co_ors = get_coordinates()
    debug_log(co_ors)
    city, country = location_details(co_ors[0], co_ors[1])
    print ("City:"+str(city)+", Country:"+str(country))


