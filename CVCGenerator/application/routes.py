from flask import Flask, request
from application import app
import requests
import random

numbers = '0123456789'

@app.route('/post-cvc', methods=['POST'])
def post_cvc():
	country = request.get_json()["Country"]
	response_value = ''.join(random.choice(numbers) for i in range(3))
	return {"CVC":response_value}

