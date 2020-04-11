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

    if args[0] == 'http://country-service:5004/post-sort-PK/':
    	return MockResponse({"Sort": "70-71-65"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-BL/':
    	return MockResponse({"Sort": "71-83-93"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-UK/':
    	return MockResponse({"Sort": "72-89-37"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-UE/':
    	return MockResponse({"Sort": "73-49-59"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-SK/':
    	return MockResponse({"Sort": "74-53-45"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-IT/':
    	return MockResponse({"Sort": "75-50-93"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-CH/':
    	return MockResponse({"Sort": "76-83-57"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-IN/':
    	return MockResponse({"Sort": "77-49-08"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-SG/':
    	return MockResponse({"Sort": "77-95-80"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-DK/':
    	return MockResponse({"Sort": "78-35-89"}, 200)
    elif args[0] == 'http://country-service:5004/post-sort-SW/':
    	return MockResponse({"Sort": "79-08-60"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_PK(self, mock_get):
		#Assert requests.get calls
		pre_ibanPK = requests.get('http://country-service:5004/post-sort-PK/').json()
		self.assertEqual(pre_ibanPK, {"Sort": "70-71-65"})
	
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_BL(self, mock_get):
		pre_ibanBL = requests.get('http://country-service:5004/post-sort-BL/').json()
		self.assertEqual(pre_ibanBL, {"Sort": "71-83-93"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_UK(self, mock_get):
		pre_ibanUK = requests.get('http://country-service:5004/post-sort-UK/').json()
		self.assertEqual(pre_ibanUK, {"Sort": "72-89-37"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_UE(self, mock_get):
		pre_ibanUE = requests.get('http://country-service:5004/post-sort-UE/').json()
		self.assertEqual(pre_ibanUE, {"Sort": "73-49-59"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_SK(self, mock_get):
		pre_ibanSK = requests.get('http://country-service:5004/post-sort-SK/').json()
		self.assertEqual(pre_ibanSK, {"Sort": "74-53-45"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_IT(self, mock_get):
		pre_ibanIT = requests.get('http://country-service:5004/post-sort-IT/').json()
		self.assertEqual(pre_ibanIT, {"Sort": "75-50-93"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_CH(self, mock_get):
		pre_ibanCH = requests.get('http://country-service:5004/post-sort-CH/').json()
		self.assertEqual(pre_ibanCH, {"Sort": "76-83-57"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_IN(self, mock_get):
		pre_ibanIN = requests.get('http://country-service:5004/post-sort-IN/').json()
		self.assertEqual(pre_ibanIN, {"Sort": "77-49-08"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_SG(self, mock_get):
		pre_ibanSG = requests.get('http://country-service:5004/post-sort-SG/').json()
		self.assertEqual(pre_ibanSG, {"Sort": "77-95-80"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_DK(self, mock_get):
		pre_ibanDK = requests.get('http://country-service:5004/post-sort-DK/').json()
		self.assertEqual(pre_ibanDK, {"Sort": "78-35-89"})

	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_SW(self, mock_get):
		pre_ibanSW = requests.get('http://country-service:5004/post-sort-SW/').json()
		self.assertEqual(pre_ibanSW, {"Sort": "79-08-60"})


if __name__ == '__main__':
	unittest.main()
