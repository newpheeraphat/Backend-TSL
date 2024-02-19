import os.path
import re

import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS

from classify_main import *
from url_main import *
from utils.helpers import *
from website_main import *
from datasources.classify_datasource import Classification

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['POST'])
def predict():
    data = request.json
    url = data['url']
    path = data['path']
    
    if url == '': 
      return ''
    
    print(f"URL: {url}")

    verify = Classification()
    # Scraping
    url = make_request(url)
    text = verify.extract_data_from_url(url)

    if path == "verification":
      response_data = {
        "classify": classify(text),
        "url_detection": get_prediction_from_url(url)
      }
    elif path == 'report':
      response_data = {
        "classify": classify(text),
        "meta_website": text
      }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=False, port=8000)
