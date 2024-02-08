import re
import socket
import ssl
import whois
import requests
import urllib.request
from urllib.parse import urlparse
from datetime import datetime
from utils.helpers import *
from tranco import Tranco

class WebsiteData: 
    def __init__(self, url: str) -> None: 
      self.url = url
      self.web = make_request(self.url)
      self.response = requests.get(self.web)
      self.page = get_tag_information(self.web)
        
    def get_alexa_rank(self):
      try: 
        api_url = "https://api.codetabs.com/v1/alexa"
        query_parameters = {"web": self.url}
        response = requests.get(api_url, params=query_parameters)
        
        if response.status_code == 200:
          api_data = response.json()
          return api_data['rank']
        else:
          print("API request failed with status code:", response.status_code)   
      except Exception as e:
        return f"error: {e}"

    def get_tranco_rank(self): 
      try:
        t = Tranco(cache=True, cache_dir='.tranco')
        latest_list = t.list()
        return latest_list.rank(remove_www(self.url))
      except Exception as e:
        return f"error: {e}"
            
    def get_ip_address(self): 
      try:
        return socket.gethostbyname(self.url)
      except Exception as e:
        return "No IP Address: {e}"
    
    def get_meta_tag_title(self) -> None: 
      try:
        title = str(self.page.get_metadatas('title'))
        if title.startswith('[') and title.endswith(']'):
          title = title[1:-1]
        if title.startswith("'") and title.endswith("'"):
          title = title[1:-1]
        return title
      except Exception as e: 
        return f"Error: {e}"
    
    def get_meta_tag_desc(self) -> None: 
      try:
        desc = str(self.page.get_metadatas('description'))
        if desc.startswith('[') and desc.endswith(']'):
          desc = desc[1:-1]
        if desc.startswith("'") and desc.endswith("'"):
          desc = desc[1:-1]
        return desc
      except Exception as e: 
        return f"Error: {e}"
    
    def get_status_code(self) -> None:
      try:
        return self.response.status_code
      except Exception as e: 
        return f"An error occurred: {e}"

    def get_domain_age(self) -> None:
      try:
        domain_info = whois.whois(self.url)
        if domain_info.creation_date and isinstance(domain_info.creation_date, list):
          creation_date = domain_info.creation_date[0]
        else:
          creation_date = domain_info.creation_date

        if creation_date:
          current_date = datetime.now()
          age = current_date.year - creation_date.year - ((current_date.month, current_date.day) < (creation_date.month, creation_date.day))
          return age
        else:
          return "Creation date not available"
      except Exception as e: 
        return "Creation date not available"

    def check_ssl_certificate(self, port=443):
      try:
          context = ssl.create_default_context()
          with socket.create_connection((self.url, port)) as sock:
              with context.wrap_socket(sock, server_hostname=self.url) as ssock:
                  certificate = ssock.getpeercert()
                  if certificate:
                      expiry_date = datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
                      return "Valid" if expiry_date > datetime.now() else "Expired"
                  else:
                      return "No certificate found"
      except Exception as e: 
          return "No certificate found"
        
    def get_certificate_type(self, port=443):
      try:
        context = ssl.create_default_context()
        
        with socket.create_connection((self.url, port)) as sock:
            with context.wrap_socket(sock, server_hostname=self.url) as ssock:
              cert = ssock.getpeercert()
              subject = dict(x[0] for x in cert['subject'])
              issuer = dict(x[0] for x in cert['issuer'])
            extended_key_usage = cert.get('extendedKeyUsage')
            
            # DV certificates usually have less information and no organizationName
            if 'organizationName' not in subject:
              cert_type = 'Domain Validated (DV)'
            # OV certificates have an organizationName but lack extendedKeyUsage specific to EV
            elif 'organizationName' in subject and (not extended_key_usage or 'TLS Web Server Authentication' in extended_key_usage):
              cert_type = 'Organization Validated (OV)'
            # EV certificates have extendedKeyUsage and specific issuer attributes
            elif 'organizationName' in subject and extended_key_usage and ('TLS Web Server Authentication' in extended_key_usage):
              cert_type = 'Extended Validation (EV)'
            else:
              cert_type = 'Unknown'
            
            return cert_type
      except Exception as e:
        return "No type of certificate found"

    def get_whois_registration_date(self):
      try:
        domain_info = whois.whois(self.url)
        if isinstance(domain_info.creation_date, list):
          registration_date = domain_info.creation_date[0]
        else:
          registration_date = domain_info.creation_date
        if isinstance(registration_date, datetime):
          registration_date = registration_date.strftime('%Y-%m-%d')
        return registration_date
      except Exception as e:
        return f"An error occurred: {e}"

    def get_whois_last_updated(self):
      try:
        domain_info = whois.whois(self.url)
        if domain_info.updated_date:
          if isinstance(domain_info.updated_date, list):
              last_updated = max(domain_info.updated_date)
          else:
              last_updated = domain_info.updated_date
            
          if isinstance(last_updated, datetime):
            return last_updated.strftime('%Y-%m-%d')
          else:
            return last_updated
        else: 
          return "No update date available."
      except Exception as e: 
        return f"An error occurred: {e}"
    
    def get_whois_renewal_date(self):
      try:
        w = whois.whois(self.url)
        if w.expiration_date:
          if isinstance(w.expiration_date, list):
              renew_date = w.expiration_date[0]
          else:
              renew_date = w.expiration_date

          if isinstance(renew_date, datetime):
              return renew_date.strftime('%Y-%m-%d')
          else:
              return str(renew_date)
        else:
            return "Renewal date not available."
      except Exception as e:
        return f"An error occurred: {e}"
    
    def get_redirected_domains(self):
      try:
        response = requests.get(self.web, allow_redirects=True)
        redirect_chain = [r.url for r in response.history]  # Get the list of redirects
        redirect_chain.append(response.url)  # Add the final destination URL
        return redirect_chain
      except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

    def is_whois_hidden(self):
      try:
          w = whois.whois(self.url)
          if not w.registrant_name or w.registrant_name in ['REDACTED FOR PRIVACY', 'Privacy service provided by']:
              return 'protected'
          if not w.emails or any('privacy' in email for email in w.emails):
              return 'protected'
          return 'hidden'
      except Exception as e:
          return str(e)