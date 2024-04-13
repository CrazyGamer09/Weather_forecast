from django.test import TestCase
from .api_client import API_CLIENT

# Create your tests here.
class API_Test(TestCase):

    def test_api_call(self):
        # calling the weater api one time call
        api_obj = API_CLIENT()
        data = api_obj.fetch_weather(lat=33.44, lon=-94.04)
        assert(data, "called")