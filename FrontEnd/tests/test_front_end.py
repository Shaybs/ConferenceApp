import unittest
import requests
from unittest import mock
from flask import abort, url_for
from flask_testing import TestCase
import os
from application import app, db
from application.models import Users
from flask_login import login_user, current_user, logout_user, login_required

class TestBase(TestCase):

	def create_app(self):

		#Passes in test configurations
		config_name = 'testing'
		app.config.update(
			SQLALCHEMY_DATABASE_URI="mysql+pymysql://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@"+os.getenv("MYSQL_URL")+"/"+os.getenv("MYSQL_DB_TEST")
		)
		return app

	def setUp(self):

		#Called before every test
		db.session.commit()
		db.drop_all()
		db.create_all()

		#Create test admin user
		admin = Users(first_name="admin", last_name="admin", username="admin", email="admin@admin.com", password="admin")
		employee = Users(first_name="test", last_name="user", username="employee", email="test@user.com", password="test2016")

		#Save/Add users to the databse
		db.session.add(admin)
		db.session.add(employee)

		db.session.commit()

	def tearDown(self):
		#Called after every test
		db.session.remove()
		db.drop_all()

class TestUpdate(TestBase):

	def test_update_account(self):
		#Place the second row of the users table into the employee
		employee = Users.query.filter_by(id=2)

		#This creates a list of rows, hence the variable's first row must be called
		employee[0].first_name = "NotTest"
		employee[0].last_name = "NotUser"
		employee[0].email = "NotTest@NotUser.com"

		#Committing the new input into the SQL table
		db.session.commit()

		#Getting the new row from the SQL database
		employee = Users.query.filter_by(id=2)

		#Testing the whether the values match previous values
		self.assertNotEqual(employee[0].first_name, "test")
		self.assertNotEqual(employee[0].last_name, "user")
		self.assertNotEqual(employee[0].email, "test@user.com")


class ModelTests(TestBase):
	
	#Test whether a new list can be added and the count of the table to verify the addition
	def test_users_model(self):
		piers = Users(first_name="piers", last_name="gilbert", email="piers@email.com", password="unknown")
		db.session.add(piers)
		db.session.commit()
		self.assertEqual(Users.query.count(), 3)

	#Test whether a row can be deleted and the count of the table to verify the deletion
	def test_users_delete_model(self):
		Users.query.filter(Users.id == 1).delete()
		db.session.commit()
		self.assertEqual(Users.query.count(), 1)

class TestViews(TestBase):

	#Test the HTTP response for the home page
	def  test_home_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the login page
	def  test_login_view(self):
		response = self.client.get(url_for('login'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the register page
	def  test_register_view(self):
		response = self.client.get(url_for('register'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the about page
	def  test_about_view(self):
		response = self.client.get(url_for('about'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the account page
	def  test_account_view(self):
		response = self.client.get(url_for('account'))
		self.assertEqual(response.status_code, 302)

	#Test the HTTP response for the account page
	def  test_account_view(self):
		response = self.client.get(url_for('accountgenerator'))
		self.assertEqual(response.status_code, 302)

	#Test the HTTP response for the logout page
	def  test_logout_view(self):
		response = self.client.get(url_for('logout'))
		self.assertEqual(response.status_code, 302)

class TestFrontEnd(TestBase):
    #Test the string response of the Home page
	def test_home_route_works_as_expected(self):
		response = self.client.get(url_for('home'))
		self.assertIn(b"Home Page", response.data)

	#Test the string response of the About page
	def test_about_route_works_as_expected(self):
		response = self.client.get(url_for('about'))
		self.assertIn(b"About", response.data)

	#Test the string response for the register
	def test_register_route_works_as_expected(self):
		response = self.client.get(url_for('register'))
		self.assertIn(b"Register for an account", response.data)

	#Test the string response for the login
	def test_login_route_works_as_expected(self):
		response = self.client.get(url_for('login'))
		self.assertIn(b"Login", response.data)

class ModelTests(TestBase):
	
	#Test whether a new list can be added and the count of the table to verify the addition
	def test_users_model(self):
		piers = Users(first_name="piers", last_name="gilbert", username="gilbert", email="piers@email.com", password="unknown")
		db.session.add(piers)
		db.session.commit()
		self.assertEqual(Users.query.count(), 3)

	#Test whether a row can be deleted and the count of the table to verify the deletion
	def test_users_delete_model(self):
		Users.query.filter(Users.id == 1).delete()
		db.session.commit()
		self.assertEqual(Users.query.count(), 1)

class TestLogin(TestBase):
	# Ensure that the account page requires user login
	def test_account_route_requires_login(self):
		response = self.client.get(url_for('account'), follow_redirects=True)
		self.assertIn(b'Login', response.data)

	# Test whether login works properly
	def test_login(self):
		response = self.client.post(
			url_for('login'),
			data=dict(email="admin@admin.com", password="admin"),
			follow_redirects=True
		)
		self.assertIn(b'', response.data)
		self.assertEqual(response.status_code, 200)

	# Test whether registration works properly
	def test_register(self):
		response = self.client.post(
			url_for('login'),
			data=dict(first_name="test", last_name="anothername", username="gilbert", email="newadmin@admin.com", password="unknown"),
			follow_redirects=True
		)
		self.assertIn(b'', response.data)
		self.assertEqual(response.status_code, 200)

	# Test whether logout works
	def test_logout(self):
		return self.client.get(url_for('logout'), follow_redirects=True)


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code 

        def json(self):
            return self.json_data

    if args[0] == 'http://central-service:5000/post-iban-PK/':
    	return MockResponse({"IBAN": "PK78NVYV605291235VEY9REJVH6K"}, 200)
    elif args[0] == 'http://central-service:5000/post-iban-IT':
    	return MockResponse({"IBAN": "IT78CCQE6585255894U347013A950"}, 200)
    elif args[0] == 'http://central-service:5000/post-iban-DK':
    	return MockResponse({"IBAN": "DK22FSFT683592381GDZ3RUI53M93A"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_PK(self, mock_get):
		#Assert requests.get calls
		ibanPK = requests.get('http://central-service:5000/post-iban-PK/').json()
		self.assertEqual(ibanPK, {"IBAN": "PK78NVYV605291235VEY9REJVH6K"})
	
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_IT(self, mock_get):
		ibanIT = requests.get('http://central-service:5000/post-iban-IT').json()
		self.assertEqual(ibanIT, {"IBAN": "IT78CCQE6585255894U347013A950"})
	
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_DK(self, mock_get):
		ibanDK = requests.get('http://central-service:5000/post-iban-DK').json()
		self.assertEqual(ibanDK, {"IBAN": "DK22FSFT683592381GDZ3RUI53M93A"})

if __name__ == '__main__':
	unittest.main()
