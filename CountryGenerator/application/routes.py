from flask import Flask, request
from application import app
import requests
import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

@app.route('/post-iban-4', methods=['POST'])
def post_iban4():
	country = request.get_json()["Country"]
	if country == "Pakistan":
		initial = "PK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "Belarus":
		initial = "BL"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "United Kingdom":
		initial = "UK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "United Arab Emirates":
		initial = "UE"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "South Korea":
		initial = "SK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "Italy":
		initial = "IT"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "China":
		initial = "CH"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "India":
		initial = "IN"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "Singapore":
		initial = "SN"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "Denmark":
		initial = "DK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}
	elif country == "Switzerland":
		initial = "SW"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + value1_string + value2_string
		return {"IBAN":response_value}

@app.route('/post-iban-8', methods=['POST'])
def post_iban8():
	country = request.get_json()["Country"]
	if country == "Pakistan":
		initial = "PK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "Belarus":
		initial = "BL"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "United Kingdom":
		initial = "UK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "United Arab Emirates":
		initial = "UE"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "South Korea":
		initial = "SK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "Italy":
		initial = "IT"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "China":
		initial = "CH"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "India":
		initial = "IN"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "Singapore":
		initial = "SN"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "Denmark":
		initial = "DK"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}
	elif country == "Switzerland":
		initial = "SW"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		random_letters = ''.join(random.choice(letters) for i in range(4))
		response_value = initial + value1_string + value2_string + random_letters
		return {"IBAN":response_value}

