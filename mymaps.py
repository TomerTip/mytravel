import googlemaps
from datetime import datetime

def get_best_location_estimation(gmaps_result):
    blacklist_types = ['political', 'sublocality']
    for result in gmaps_result:
        if any(type in blacklist_types for type in result["types"]):
            continue
        else:
            return result

gmaps = googlemaps.Client(key='AIzaSyAuFGMlJLrLutpttzvFIp9mAlkb5mVpYNk')

import ipdb;ipdb.set_trace()
# Geocoding an address
city = "Rio De Janiero"
place = "Ipanema"
lat, long = ('-22.987', '-43.213')

import ipdb;ipdb.set_trace()

place_result = gmaps.places_autocomplete_query(input_text=f'{city}, {place}', location=f'{lat},{long}')
place_result = get_best_location_estimation(place_result)
print(place_result)
'''
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)
'''