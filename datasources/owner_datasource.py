import socket
import ssl

class Owner: 
  def __init__(self, url: str) -> None: 
    self.url = url
  
  def get_organization_name(self, port=443):
    try:
      context = ssl.create_default_context()
      
      with socket.create_connection((self.url, port)) as sock:
          with context.wrap_socket(sock, server_hostname=self.url) as ssock:
              cert = ssock.getpeercert()
              issuer = dict(x[0] for x in cert['issuer'])
          # DV certificates usually have less information and no organizationName
          return issuer['organizationName']
    except Exception as e:
      return "Not found organization name"

  def get_country(self, port=443):
    try:
      context = ssl.create_default_context()
      
      with socket.create_connection((self.url, port)) as sock:
          with context.wrap_socket(sock, server_hostname=self.url) as ssock:
              cert = ssock.getpeercert()
              issuer = dict(x[0] for x in cert['issuer'])
          # DV certificates usually have less information and no organizationName
          return issuer['countryName']
    except Exception as e: 
      return "Not found country name"
      
  def get_CA(self, port=443):
    try:
      context = ssl.create_default_context()
      
      with socket.create_connection((self.url, port)) as sock:
          with context.wrap_socket(sock, server_hostname=self.url) as ssock:
              cert = ssock.getpeercert()
              issuer = dict(x[0] for x in cert['issuer'])
          # DV certificates usually have less information and no organizationName
          return issuer['commonName']
    except Exception as e: 
      return "Not found common name"