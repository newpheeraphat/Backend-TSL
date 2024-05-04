from datasources.websitedata_datasource import WebsiteData
from datasources.measurement_datasource import RiskAssessment
from utils.helpers import *

import utils.constants as c

def run(raw_url: str):
  try:
    url = get_domain_name(raw_url)
    website = WebsiteData(url)
    measurement = RiskAssessment()
    
    country = website.get_country()
    tld = website.get_tld()
    registrar = website.get_domain_registration()
  
    
    response_data = {
      'measurement': {
        "is_risk_country": measurement.is_risk_country_measurement(country),
        "is_risk_tld": measurement.is_risk_tld_measurement(tld),
        "is_risk_registrar": measurement.is_risk_registrar_measurement(registrar)
      }
    }
    
    return response_data
  except Exception as e: 
    print("Error Occurred with Website Detail" + e)
    return {
      'measurement': {
        "is_risk_country": False,
        "is_risk_tld": False,
        "is_risk_registrar": False
      }
    }
