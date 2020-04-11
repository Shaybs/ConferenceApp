from application import app
import unittest
from flask_testing import TestCase
import requests
from unittest import mock


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code 

        def json(self):
            return self.json_data

    if args[0] == 'http://card-service:5005/post-cardnumber':
    	return MockResponse({"CardNumber": "9374897238974267"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_cardnumber(self, mock_get):
		#Assert requests.get calls
		cardnumber = requests.get('http://card-service:5005/post-cardnumber').json()
		self.assertEqual(cardnumber, {"CardNumber": "9374897238974267"})

if __name__ == '__main__':
	unittest.main()