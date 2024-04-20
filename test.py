from flask import Flask, jsonify, request
from flask_cors import CORS
from mainsources.classify_main import *
from mainsources.url_main import *
from mainsources.website_main import *
from utils.helpers import *

app = Flask(__name__)
CORS(app) 

def predict(url: str):
    data = {
      "url": url,
      "path": "verification"
    }
    raw_url = data.get('url', '')  # use .get for safer retrieval of dict keys
    action = data.get('path', '')

    raw_url = make_request(raw_url) # add http or https
    
    if not raw_url:  
        return jsonify({"error": "URL is required."}), 400
    
    print(f"Processing URL: {raw_url}")
    
    verifier = Classification() 
    
    try:
        response_url = make_request(raw_url)
        response_url = redirect_to_homepage(response_url)

        print(response_url)
        extracted_data = verifier.extract_data_from_url(response_url)
    except Exception as e:  
        return jsonify({"error": str(e)}), 500  

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

if __name__ == '__main__':
    # predict("facebook.com/")
    predict("https://www.google.com/search?q=fdsaff&sca_esv=2465539c7fa84006&source=hp&ei=9c4WZufcHbyNseMP4rmX6Aw&iflsig=ANes7DEAAAAAZhbdBZ4X0uzihry1pRV1l6rh7IZZoReb&ved=0ahUKEwinq8W7mLiFAxW8RmwGHeLcBc0Q4dUDCA0&uact=5&oq=fdsaff&gs_lp=Egdnd3Mtd2l6IgZmZHNhZmYyCRAAGIAEGA0YCkjXBVA7WJsEcAF4AJABAJgBbqAB6gOqAQM1LjG4AQPIAQD4AQGYAgegAokEqAIKwgIQEAAYAxiPARjlAhjqAhiMA8ICEBAuGAMYjwEY5QIY6gIYjAPCAhEQLhiDARjHARixAxjRAxiABMICCxAAGIAEGLEDGIMBwgIREC4YgAQYsQMYgwEYxwEY0QPCAhcQLhiABBiKBRixAxiDARjHARivARiOBcICDhAAGIAEGIoFGLEDGIMBwgIFEAAYgATCAhEQLhiABBjHARivARiYBRiZBcICBxAAGIAEGAqYAwySBwM2LjGgB-cg&sclient=gws-wiz")