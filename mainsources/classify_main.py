from datasources.classify_datasource import Classification
from utils.helpers import *

def classify(text):
  try: 
    classify = Classification()
    # url = make_request(raw_url)
    # text = classify.extract_data_from_url(url)
    df = classify.convert_to_dataframe(text)
    verification = classify.verify_website(df)
    
    return verification
  except Exception as e: 
    print(f"Failed occurred: {e}")
    return {}
    
    
