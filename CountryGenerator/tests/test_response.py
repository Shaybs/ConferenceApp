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

    if args[0] == 'http://country-service:5001/post-iban-4/':
    	return MockResponse({"IBAN": "PK67"}, 200)
    elif args[0] == 'http://country-service:5001/post-iban-8/':
    	return MockResponse({"IBAN": "IT56NKJS"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_PK(self, mock_get):
        pre_ibanPK = requests.get('http://country-service:5001/post-iban-4/').json()
        self.assertEqual(pre_ibanPK, {"IBAN": "PK67"})

    
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_IT(self, mock_get):
        pre_ibanIT = requests.get('http://country-service:5001/post-iban-8/').json()
        self.assertEqual(pre_ibanIT, {"IBAN": "IT56NKJS"})

if __name__ == '__main__':
	unittest.main()

