from datasources.websitedata_datasource import WebsiteData
from datasources.measurement_datasource import RiskAssessment

import utils.constants as c
from utils.helpers import get_domain_name

def display_website_insight(website_insights):
  print(f"Country: {website_insights[0]}")
  print(f"Top Level Domain: {website_insights[1]}")
  print(f"Registrar: {website_insights[2]}")

def run(raw_url: str):
    url = get_domain_name(raw_url)
    website = WebsiteData(url)
    measurement = RiskAssessment()
    
    country = website.get_country()
    tld = website.get_tld()
    registrar = website.get_domain_registration()
    display_website_insight([country, tld, registrar])
  
    
    response_data = {
      'measurement': {
        "is_risk_country": measurement.is_risk_country_measurement(country),
        "is_risk_tld": measurement.is_risk_tld_measurement(tld),
        "is_risk_registrar": measurement.is_risk_registrar_measurement(registrar)
      }
    }
    
    return response_data
