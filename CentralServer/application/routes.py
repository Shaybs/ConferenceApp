from flask import Flask, request
from application import app
import requests
import random

numbersletters = '0A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0U1V2W3X4Y5Z'

@app.route('/get-account6', methods=['GET','POST'])
def test_account6():	
	account = requests.post('http://account-service:5002/post-account-6', json={"Country":"Pakistan"})
	if account.ok:
		return account.json()["Account"]
	return "OK\n"

@app.route('/get-account8', methods=['GET','POST'])
def test_account8():	
	account = requests.post('http://account-service:5002/post-account-8', json={"Country":"Pakistan"})
	if account.ok:
		return account.json()["Account"]
	return "OK\n"

@app.route('/get-iban4', methods=['GET','POST'])
def test_iban4():
	iban = requests.post('http://country-service:5001/post-iban-4', json={"Country":"Belarus"})
	if iban.ok:
		return iban.json()["IBAN"]
	return "OK\n"

@app.route('/get-iban8', methods=['GET','POST'])
def test_iban8():
	iban = requests.post('http://country-service:5001/post-iban-8', json={"Country":"Belarus"})
	if iban.ok:
		return iban.json()["IBAN"]
	return "OK\n"

@app.route('/post-iban', methods=['POST'])
def post_iban():
	country = request.get_json()["Country"]
	card_cvc = requests.post('http://cvc-service:5006/post-cvc', json={"Country":country})
	cvc = card_cvc.json()["CVC"]
	card_cardnumber = requests.post('http://cardnumber-service:5005/post-cardnumber', json={"Country":country})
	cardnumber = card_cardnumber.json()["CardNumber"]
	card_sort = requests.post('http://sort-service:5004/post-sort', json={"Country":country})
	sort = card_sort.json()["Sort"]
	account = requests.post('http://account-service:5002/post-account-8', json={"Country":country})
	iban_account = account.json()["Account"]
	iban_preambleservice = requests.post('http://country-service:5001/post-iban-8', json={"Country":country})
	iban_preamble = iban_preambleservice.json()["IBAN"]

	if iban_preamble[0] == 'P' and iban_preamble[1] == 'K':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(12))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'B' and iban_preamble[1] == 'L':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(12))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'U' and iban_preamble[1] == 'K':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(12))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'U' and iban_preamble[1] == 'E':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(12))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'S' and iban_preamble[1] == 'K':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(12))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'I' and iban_preamble[1] == 'T':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(13))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'C' and iban_preamble[1] == 'H':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(14))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'I' and iban_preamble[1] == 'N':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(14))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'S' and iban_preamble[1] == 'N':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(14))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'D' and iban_preamble[1] == 'K':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(14))
		iban = iban_preamble + iban_account + iban_numbers_in_string
	elif iban_preamble[0] == 'S' and iban_preamble[1] == 'W':
		iban_numbers_in_string = ''.join(random.choice(numbersletters) for i in range(14))
		iban = iban_preamble + iban_account + iban_numbers_in_string

	return {"IBAN":iban, "BankAccount":iban_account, "Sort":sort, "CardNumber":cardnumber, "CVC":cvc}



