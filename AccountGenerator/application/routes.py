from flask import Flask, request
from application import app
import requests
import random

@app.route('/post-account-6', methods=['POST'])
def post_account6():
	country = request.get_json()["Country"]
	if country == "Pakistan":
		initial = "60"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Belarus":
		initial = "61"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "United Kingdom":
		initial = "62"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "United Arab Emirates":
		initial = "63"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "South Korea":
		initial = "64"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Italy":
		initial = "65"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "China":
		initial = "66"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "India":
		initial = "67"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Singapore":
		initial = "67"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Denmark":
		initial = "68"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Switzerland":
		initial = "69"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}

@app.route('/post-account-8', methods=['POST'])
def post_account8():
	country = request.get_json()["Country"]
	if country == "Pakistan":
		initial = "60"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "Belarus":
		initial = "61"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "United Kingdom":
		initial = "62"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "United Arab Emirates":
		initial = "63"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "South Korea":
		initial = "64"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "Italy":
		initial = "65"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "China":
		initial = "66"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "India":
		initial = "67"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "Singapore":
		initial = "67"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "Denmark":
		initial = "68"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
	elif country == "Switzerland":
		initial = "69"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		value5 = random.randint(1,9)
		value5_string = str(value5)
		value6 = random.randint(1,9)
		value6_string = str(value6)
		response_value = initial + value1_string + value2_string + value3_string + value4_string + value5_string + value6_string
		return {"Account":response_value}
