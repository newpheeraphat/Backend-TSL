from utils.helpers import *
import os
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
            print(f"No IP Address found for {self.url}: {e}")
            return None

    def get_country(self): 
        ip_address = self.get_ip_address()
        if not ip_address:
            print("This webpage has no IP address.")
            return ""

        try:
            with geoip2.database.Reader('./dataset/GeoLite2-Country.mmdb') as reader:
                response = reader.country(ip_address)
                return response.country.name or ""
        except Exception as e: 
            print(f"Error occurred while getting country: {e}")
            return ""
    
    def get_domain_registration(self):
        domain_name = get_domain_name(self.url)  
        if not domain_name:
            print(f"Domain name could not be extracted from URL: {self.url}")
            return ""

        try:
            domain_info = whois.whois(domain_name)
            return domain_info.registrar or ""
        except Exception as e:
            print(f"Error occurred while getting registrar information: {e}")
            return ""
    
    def get_tld(self):
        try: 
            extracted = tldextract.extract(self.url)
            return f".{extracted.suffix}" if extracted.suffix else ""
        except Exception as e:
            print(f"Error occurred while getting top-level domain: {e}")
            return ""