from datasources.websitedata_datasource import WebsiteData
from datasources.measurement_datasource import Measurement
from utils.helpers import *

import utils.constants as c

def display_data(lstS): 
  print(f"Country: {lstS[0]}")
  print(f"Top Level Domain: {lstS[1]}")
  print(f"Registrar: {lstS[2]}")


def run(raw_url):
    url = preprocessing_url(raw_url)
    website = WebsiteData(url)
    measurement = Measurement()
    
    country = website.get_country()
    tld = website.get_tld()
    registar = website.get_domain_registration()

    response_data = {
      'measurement': {
        "is_risk_country": measurement.is_risk(country, c.RISK_COUNTRIES_URL),
        "is_risk_tld": measurement.is_risk(tld, c.TOP_LEVEL_DOMAINS_URL),
        "is_risk_registrar": measurement.is_risk(registar, c.REGISTRAR_URL)
      }
    }
    
    return response_data;
