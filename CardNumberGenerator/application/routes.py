from flask import Flask, request
from application import app
import requests
import random

numbers = '0123456789'

@app.route('/post-cardnumber', methods=['POST'])
def post_cardnumber():
	country = request.get_json()["Country"]
	response_value = ''.join(random.choice(numbers) for i in range(16))
	return {"CardNumber":response_value}
