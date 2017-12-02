from __future__ import print_function

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.locations_api import LocationsApi

# setup authorization
squareconnect.configuration.access_token = 'sandbox-sq0atb-SBlt7uuJdLR8LzsuVmeXCw'
# create an instance of the Location API class
api_instance = LocationsApi()

try:
    # ListLocations
    api_response = api_instance.list_locations()
    print (api_response.locations)
except ApiException as e:
    print ('Exception when calling LocationApi->list_locations: %s\n' % e)
