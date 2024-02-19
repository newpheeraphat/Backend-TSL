from utils.helpers import *

import socket
import tldextract
import geoip2.database
import whois
class WebsiteData: 
    def __init__(self, url: str) -> None: 
      self.url = url
      self.web = make_request(self.url)
            
    def get_ip_address(self): 
      try:
        return socket.gethostbyname(self.url)
      except Exception as e:
        return "No IP Address: {e}" 
    
    def get_country(self): 
      try:
        with geoip2.database.Reader('/Users/pheeraphatprisan/Desktop/Sourcetree/Backend-TSL/dataset/GeoLite2-Country.mmdb') as reader:
          response = reader.country(self.get_ip_address())
          return response.country.name
      except Exception as e: 
        print("Error Occurred: " + e)
        return ""
    
    def get_domain_registration(self):
      try:
          domain_info = whois.whois(preprocessing_url_detection(self.url))
          return domain_info.registrar
      except Exception as e:
          print("Error Ocurred: " + e) 
          return None
    
    def get_tld(self):
      try: 
        extracted = tldextract.extract(self.web)
        tld = ".{}".format(extracted.suffix) 
        return tld
      except Exception as e:
        print("Error Occurred: " + e)
        return ""