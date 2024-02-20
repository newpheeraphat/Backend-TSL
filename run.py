from classify_main import *
from flask import Flask, jsonify, request
from flask_cors import CORS
from mainsources.classify_main import *
from mainsources.url_main import *
from mainsources.website_main import *
from url_main import *
from utils.helpers import *

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['POST'])
def redict():
    data = request.json
    raw_url = data['url']
    path = data['path']
    
    if raw_url == '':
      return ''
    
    print(f"URL: {raw_url}")
    
    verify = Classification()
    url = make_request(raw_url) # Add HTTP
    text = verify.extract_data_from_url(url) # Scraping Meta data and all text in the website

    if path == "verification":
      response_data = {
        "currentPercent": classify(text),
        "urlDetection": get_prediction_from_url(url),
        "isRisk": run(url)
      }
    elif path == "report": 
      response_data = {
        "classify": classify(text),
        "meta_website": text
      }
  
      
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=False, port=8000)
