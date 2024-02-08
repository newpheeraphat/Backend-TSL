import whois
import subprocess
import re

class Registrar: 
  def __init__(self, url: str) -> None: 
    self.url = url
  
  def get_domain_registrar(self):
    try:
      domain_info = whois.whois(self.url)
      registrar = domain_info.registrar
      return registrar if registrar else "Registrar not found."
    except Exception as e:
      return f"An error occurred: {e}"
      
      
  def get_iana_id(self):
    try:
      result = subprocess.run(['whois', self.url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      whois_output = result.stdout.decode()
      match = re.search(r'IANA ID: (\d+)', whois_output)
      if match:
        return match.group(1)
      else:
        return "IANA ID not found."
    except Exception as e: 
      return f"An error occurred: {e}"
  
  def get_email(self):
      try:
        w = whois.whois(self.url)
        if isinstance(w.emails, list) and w.emails:
          return w.emails[0]
        return w.emails
      except Exception as e:
        return f"An error occurred: {e}"