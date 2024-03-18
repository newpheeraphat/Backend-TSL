from datasources.classify_datasource import Classification


def classify(extracted_data):
  try: 
    classifier = Classification()
    df = classifier.convert_to_dataframe(extracted_data)
    verification_result = classifier.verify_website(df)
    return verification_result
  except Exception as e: 
    print(f"Failed occurred from classify: {e}")
    return {
      "other": 0,
      "gambling": 0,
      "scam": 0,
      "fake": 0
    }
    
    
