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

    if args[0] == 'http://account-service:5002/post-account-6':
    	return MockResponse({"Account": "609292"}, 200)
    elif args[0] == 'http://account-service:5002/post-account-8':
    	return MockResponse({"Account": "67499382"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_account6(self, mock_get):
        account6 = requests.get('http://account-service:5002/post-account-6').json()
        self.assertEqual(account6, {"Account": "609292"})

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_account8(self, mock_get):
        account8 = requests.get('http://account-service:5002/post-account-8').json()
        self.assertEqual(account8, {"Account": "67499382"})

if __name__ == '__main__':
	unittest.main()

