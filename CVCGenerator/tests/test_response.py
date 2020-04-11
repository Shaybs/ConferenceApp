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

    if args[0] == 'http://cvc-service:5006/post-cvc/':
    	return MockResponse({"CVC": "343"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_cvc(self, mock_get):
		#Assert requests.get calls
		cvc = requests.get('http://cvc-service:5006/post-cvc/').json()
		self.assertEqual(cvc, {"CVC": "343"})

if __name__ == '__main__':
	unittest.main()