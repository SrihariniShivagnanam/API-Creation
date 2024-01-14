import os
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

AGIFY_API_URL = "https://api.agify.io/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_age', methods=['POST'])
def predict_age():
    name = request.form['name']
    country = request.form['country']

    params = {
        'name': name,
        'country_id': country,
    }

    response = requests.get(AGIFY_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        age = data.get('age', 'Unknown')
        return render_template('results.html', name=name, age=age)
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
