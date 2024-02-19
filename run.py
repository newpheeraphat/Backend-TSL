from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.helpers import *
from mainsources.classify_main import *
from mainsources.website_main import *
from mainsources.url_main import *

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
        "currentPercent": classify(url),
        "urlDetection": get_prediction_from_url(url),
        "isRisk": run(url)
      }
    
    
      
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
