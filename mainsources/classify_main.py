from utils.helpers import *
from datasources.classify_datasource import Classification
from database.database import PostgreSQL

def classify(extracted_data, url):
  try: 
    classifier = Classification()
    conn = PostgreSQL()
    df = conn.retrieve_data()
    whitelist_database_data = [dict(row) for row in df]
    whitelist_urls = [get_domain_name(item['WhitelistURL']) for item in whitelist_database_data]
    get_only_domain_name_from_url = get_domain_name(url)
    
    has_url_in_whitelist_database = get_only_domain_name_from_url in whitelist_urls
    df = classifier.convert_to_dataframe(extracted_data)

    # If url exists in whitelist
    if has_url_in_whitelist_database:
       return {
        "other": 100,
        "gambling": 0,
        "scam": 0,
        "fake": 0
      }

    verification_result = classifier.verify_website(df, whitelist_database_data)
    
    
    if verification_result['fake'] > 90:
      return {
        "other": 0,
        "gambling": 0,
        "scam": 0,
        "fake": verification_result['fake']
      }
    
    return verification_result
  except Exception as e: 
    print(f"Failed occurred from classify: {e}")
    return {
      "other": 0,
      "gambling": 0,
      "scam": 0,
      "fake": 0
    }
  finally:
      conn.close_connection()
    
    
