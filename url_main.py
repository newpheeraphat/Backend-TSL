import numpy as np
from joblib import load
from tld import get_tld

from datasources.url_datasource import Url
from utils.helpers import *


def run_url(raw_url): 
  status = []
  
  raw_url = preprocessing_url_detection(raw_url)
  url = Url(raw_url)

  status.append(url.having_ip_address())
  status.append(url.abnormal_url())
  status.append(url.count_dot())
  status.append(url.count_www())
  status.append(url.count_atrate())
  status.append(url.no_of_dir())
  status.append(url.no_of_embed())

  status.append(url.shortening_service())
  status.append(url.count_https())
  status.append(url.count_http())

  status.append(url.count_per())
  status.append(url.count_ques())
  status.append(url.count_hyphen())
  status.append(url.count_equal())

  status.append(url.url_length())
  status.append(url.hostname_length())
  status.append(url.suspicious_words())
  status.append(url.digit_count())
  status.append(url.letter_count())
  status.append(url.fd_length())
  tld = get_tld(raw_url,fail_silently=True)

  status.append(url.tld_length(tld))

  return status

def load_model_in_batches(model_path, batch_size=100):
    rf_model = None
    with open(model_path, 'rb') as model_file:
        for _ in range(batch_size):
            chunk = model_file.read(1024 * 1024)  # 1 MB chunks (adjust as needed)
            if not chunk:
                break
            if rf_model is None:
                rf_model = load(chunk)
            else:
                rf_model = load(chunk, mmap_mode='r+')
    return rf_model

def get_prediction_from_url(test_url):
    features_test = run_url(test_url)

    features_test = np.array(features_test).reshape((1, -1))
  
    p = '/Users/user/Desktop/ThaiScamLinks/backend_ThaiScamLinks/Backend-TSL/model/trained_url_model.joblib'
    rf_model = load_model_in_batches(p)

    proba = rf_model.predict_proba(features_test)

    benign_proba = proba[0][0] * 100
    malicious_proba = proba[0][1] * 100

    return {"benign_proba": int(benign_proba), "malicious_proba": int(malicious_proba)}