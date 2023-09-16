import os
import keras_ocr
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify

app = Flask(__name__)
pipeline = keras_ocr.pipeline.Pipeline()

@app.get("/")
def get_index():
    return jsonify(app_status = "running")

@app.post("/ocr/image_to_text")
def post_index():
    image = request.files['file']
    prediction_groups = pipeline.recognize([ image ])
    predicted_image = prediction_groups[0]

    recognised_text = ""

    for text, box in predicted_image:
        recognised_text = recognised_text + " " + text

    return jsonify(text = recognised_text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv('PORT', 80)), threaded=True)