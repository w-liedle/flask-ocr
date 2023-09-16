# app.py
import os
from flask import Flask, request, jsonify
#import keras_ocr
#import matplotlib.pyplot as plt

app = Flask(__name__)
#pipeline = keras_ocr.pipeline.Pipeline()

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/")
def index():
    return jsonify(app_status = "running")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv('PORT', 80)), threaded=True)