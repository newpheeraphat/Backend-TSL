from datasources.classify_datasource import Classification
import pandas as pd
from utils.helpers import *

def classify(raw_url):
  try: 
    classify = Classification()
    url = make_request(raw_url)
    text = classify.extract_data_from_url(url)
    df = classify.convert_to_dataframe(text)
    verification = classify.verify_website(df)
    
    return verification
  except Exception as e: 
    print(f"Failed occurred: {e}")
    
    
