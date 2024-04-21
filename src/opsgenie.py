from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint

configuration.host = 'https://api.eu.opsgenie.com'
configuration = opsgenie_sdk.Configuration()
configuration.api_key['Authorization'] = os.environ.get('TEST_KEY')

# create an instance of the API class
api_instance = opsgenie_sdk.AccountApi(opsgenie_sdk.ApiClient(configuration))

try:
    # Get Account Info
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_info: %s\n" % e)
