import os.path
import re
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.helpers import *
from website_main import *
from classify_main import *
from url_main import *

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

    if path == "verification":
      response_data = {
        "classify": classify(url),
        "url_detection": get_prediction_from_url(url)
      }
    # elif path == "moredetail":
    #   response_data = {
    #     "website_insight": run(url),
    #   }
    elif path == 'report': 
      response_data = {
        "test": "test"
      }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
