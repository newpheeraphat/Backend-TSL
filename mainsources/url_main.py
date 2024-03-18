from datasources.url_datasource import Url
from tld import get_tld
from joblib import load
from utils.helpers import *
import requests
import numpy as np

try:
    with open('./model/trained_url_model.joblib', 'rb') as model_file:
        rf_model = load(model_file)
except Exception as e:
    print(f"Error loading model: {e}")
    rf_model = None

def run_url(raw_url): 
    url = Url(preprocessing_url_detection(raw_url))

    status_checks = [
        url.having_ip_address, url.abnormal_url, url.count_dot,
        url.count_www, url.count_atrate, url.no_of_dir, url.no_of_embed,
        url.shortening_service, url.count_https, url.count_http,
        url.count_per, url.count_ques, url.count_hyphen, url.count_equal,
        url.url_length, url.hostname_length, url.suspicious_words,
        url.digit_count, url.letter_count, url.fd_length
    ]
    
    status = [check() for check in status_checks]

    tld = get_tld(raw_url, fail_silently=True)
    status.append(url.tld_length(tld))

    return status

def get_prediction_from_url(test_url):
    if not rf_model:
        print("Model is not loaded, cannot predict URL.")
        return {"maliciousUrlPercent": 0}

    try:
        response = requests.get(test_url)
        response.raise_for_status() 
    except Exception as e:
        print(f"Failed to retrieve the webpage: {e}")
        return {"maliciousUrlPercent": 0}

    features_test = np.array(run_url(test_url)).reshape(1, -1)
    proba = rf_model.predict_proba(features_test)
    malicious_proba = proba[0][1] * 100
    return {"maliciousUrlPercent": int(malicious_proba)}
