from flask import Flask, jsonify, request
from flask_cors import CORS
from mainsources.classify_main import *
from mainsources.url_main import *
from mainsources.website_main import *
from utils.helpers import *

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['POST'])
def predict():
    data = request.json
    raw_url = data.get('url', '')  # use .get for safer retrieval of dict keys
    action = data.get('path', '')
    
    if not raw_url:  
        return jsonify({"error": "URL is required."}), 400
    
    print(f"Processing URL: {raw_url}")
    
    verifier = Classification() 
    
    try:
        response_url = make_request(raw_url)
        extracted_data = verifier.extract_data_from_url(response_url)
    except Exception as e:  
        return jsonify({"error": str(e)}), 500  

    response_data = { "meta_website": extracted_data }

    if action == "verification":
      response_data = {
        "currentPercent": classify(extracted_data),
        "urlDetection": get_prediction_from_url(response_url),
        "isRisk": run(response_url),
        "meta_website": extracted_data
      }
    elif action == "report": 
      response_data = { "classify": classify(response_url), "meta_website": extracted_data }
    else:
      return jsonify({"error": "Invalid path specified."}), 400
  
    print(response_data) 
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=False, port=8000)
