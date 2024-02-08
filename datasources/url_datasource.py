from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import urlparse
from googlesearch import search
from urllib.parse import urlparse
from tld import get_tld

import pickle
import os.path
import re
import numpy as np

class Url:
  def __init__(self, url: str) -> None: 
    self.url = url
  
  def having_ip_address(self) -> int:
    try: 
      match = re.search(
          '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
          '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
          '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
          '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', self.url)  # Ipv6
      if match:
          return 1
      else:
          return 0
    except Exception as e: 
      print("Failed Occurred in Having IP Address: ")
      return 0
  
  def abnormal_url(self) -> int:
    try:
        url_str = str(self.url)
        hostname = urlparse(url_str).hostname
        if hostname is None: return 0
        escaped_hostname = re.escape(hostname)
        match = re.search(escaped_hostname, url_str)
        return 1 if match else 0
    except Exception as e:
        print(f"Error processing URL {self.url}: {e}")
        return 0
  
  def google_index(self) -> int:
    try: 
      site = search(self.url, 5)
      return 1 if site else 0
    except Exception as e: 
      print(f"Error processsing google index {self.url}: {e}")
      return 0
  
  def count_dot(self) -> int:
    try:
      count_dot = self.url.count('.')
      return count_dot
    except Exception as e: 
      print(f"Errror processing count .: {e}")
      return 0
  
  def count_www(self) -> int:
    try:
      return self.url.count('www')
    except Exception as e: 
      print(f"Error processing count www: {e}")
      return 0

  def count_atrate(self) -> int:
    try:
      return self.url.count('@')
    except Exception as e: 
      print(f"Error processing count atrate: {e}")
      return 0
    
  def no_of_dir(self) -> int:
    try:
        url_str = str(self.url)
        urldir = urlparse(url_str).path
        return urldir.count('/')
    except ValueError as e:
        print(f"Error processing URL {self.url}: {e}")
        return 0
  
  def no_of_embed(self) -> int:
    try: 
      url_str = str(self.url)
      urldir = urlparse(url_str).path
      return urldir.count('//')
    except Exception as e: 
      print(f"Error processing count embed: {e}")
      return 0
  
  def shortening_service(self) -> int:
    try:
      match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                        'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                        'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                        'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                        'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                        'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                        'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                        'tr\.im|link\.zip\.net',
                        self.url)
      if match:
          return 1
      else:
          return 0
    except Exception as e: 
      print(f"Error processing shortening service: {e}")
      return 0
  
  def count_https(self) -> int:
    try: 
      return self.url.count('https')
    except Exception as e:
      print(f"Error processing count https: {e}")
      return 0
  
  def count_http(self) -> int:
    try:
      return self.url.count('http')
    except Exception as e:
      print(f"Error processing count http: {e}")
      return 0
    
  def count_per(self) -> int:
    try: 
      return self.url.count('%')
    except Exception as e: 
      print(f"Error processing percentage: {e}")
      return 0
    
  def count_ques(self) -> int:
    try:
      return self.url.count('?')
    except Exception as e: 
      print(f"Error processing count question mark: {e}")
      return 0
    
  def count_hyphen(self) -> int:
    try:
      return self.url.count('-')
    except Exception as e: 
      print(f"Error processing count hypen: {e}")
      return 0
    
  def count_equal(self) -> int:
    try:
      return self.url.count('=')
    except Exception as e: 
      print(f"Error processing equal: {e}")
      return 0

  def url_length(self) -> int:
    try:
      return len(str(self.url))
    except Exception as e: 
      print(f"Error processing count url length: {e}")
      return 0

  def hostname_length(self) -> int:
    try:
      return len(urlparse(self.url).netloc)
    except Exception as e: 
      print(f"Error processing count hostname length: {e}")
      return 0
  
  def suspicious_words(self) -> int:
    try:
      match = re.search('PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',
                        self.url)
      if match:
          return 1
      else:
          return 0
    except Exception as e: 
      print(f"Error processing count suspicious words: {e}")
      return 0

  def digit_count(self) -> int:
    try:
      digits = 0
      for i in self.url:
          if i.isnumeric():
              digits = digits + 1
      return digits
    except Exception as e: 
      print(f"Error processing count digit: {e}")
      return 0

  def letter_count(self) -> int:
    try:
      letters = 0
      for i in self.url:
          if i.isalpha():
              letters = letters + 1
      return letters
    except Exception as e: 
      print(f"Error processing count letter: {e}")
      return 0
  
  def fd_length(self) -> int:
    urlpath= urlparse(self.url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0


  def tld_length(self, tld) -> int:
      try:
          return len(tld)
      except:
          return -1
      
  
  