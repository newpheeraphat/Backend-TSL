from flask import Flask, request, jsonify
from utils.helpers import *
from mainsources.classify_main import *
from mainsources.website_main import *
from mainsources.url_main import *


def redict():
    data = {
      'url': "https://www.google.com",
      'path': "verification"
    }
    raw_url = data['url']
    path = data['path']
    
    if raw_url == '':
      return ''
    
    print(f"URL: {raw_url}")
    
    verify = Classification()
    url = make_request(raw_url)
    text = verify.extract_data_from_url(url) 

    if path == "verification":
      response_data = {
        "currentPercent": classify(text),
        "urlDetection": get_prediction_from_url(url),
        "isRisk": run(url),
        "meta_website": text
      }
    elif path == "report": 
      response_data = {
        "classify": classify(text),
        "meta_website": text
      }
  
      
    return jsonify(response_data)

if __name__ == '__main__':
    redict()
