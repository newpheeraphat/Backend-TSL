import os.path
import re

import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS

from classify_main import *
from url_main import *
from utils.helpers import *
from website_main import *


def predict(url):
    
    print(f"URL: {url}")

    response_data = {
    "classify": classify(url),
    # "url_detection": get_prediction_from_url(url)
    }
    # elif path == "moredetail":
    #   response_data = {
    #     "website_insight": run(url),
    #   }
    # elif path == 'report':
    #   response_data = {
    #     "test": "test"
    #   }

    return response_data

print(predict('google.com'))
# print("Hello World")
