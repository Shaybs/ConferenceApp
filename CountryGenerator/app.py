from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def get_test():
	return {"name":"Bob"}

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	return {"Country":country}

from application import app

if __name__ == '__main__':
	app.run(port=5001, host='0.0.0.0')