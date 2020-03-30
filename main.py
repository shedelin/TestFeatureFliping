from flask import Flask, flash, redirect, render_template, request, session, abort, make_response
from random import randint
import json

app = Flask(__name__)

@app.route('/')
def home():
	return  render_template('home.html')

@app.route('/featureIsOk', methods=['POST'])
def featureIsOk():
	featureId = request.form['featureId']
	country = request.form["country"]
	data = ("0", "1")["FR" == country]
	resp = make_response(json.dumps(data))
	resp.status_code = 200
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp


if __name__ == "__main__":
	app.run()