from datasources.url_datasource import Url
from tld import get_tld
from joblib import load
from utils.helpers import *

import numpy as np

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

def get_prediction_from_url(test_url):
    features_test = run_url(test_url)

    features_test = np.array(features_test).reshape((1, -1))
    
    p = open('/Users/pheeraphatprisan/Desktop/Sourcetree/Backend-TSL/model/trained_url_model.joblib', 'rb')
    rf_model = load(p)

    proba = rf_model.predict_proba(features_test)

    # benign_proba = proba[0][0] * 100
    malicious_proba = proba[0][1] * 100

    # return {"benign_proba": int(benign_proba), "malicious_proba": int(malicious_proba)}
    
    return { "maliciousUrlPercent" : int(malicious_proba) }