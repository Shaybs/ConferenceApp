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

    if args[0] == 'http://central-service:5000/post-iban':
    	return MockResponse({"IBAN":"UK74CYGK626841K8K1D4WBJ951", "BankAccount":"626841", "Sort":"72-72-03", "CardNumber":"8643182736212553", "CVC":"536"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_cardnumber(self, mock_get):
		#Assert requests.get calls
		response = requests.get('http://central-service:5000/post-iban').json()
		self.assertEqual(response, {"IBAN":"UK74CYGK626841K8K1D4WBJ951", "BankAccount":"626841", "Sort":"72-72-03", "CardNumber":"8643182736212553", "CVC":"536"})

if __name__ == '__main__':
	unittest.main()