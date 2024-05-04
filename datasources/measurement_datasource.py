from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

class RiskAssessment: 
  def __init__(self) -> None:
    self.risk_countries = [
      "United States",
      "China",
      "Russia",
      "Germany",
      "Netherlands",
      "Hong Kong",
      "Singapore",
      "United Kingdom",
      "France",
      "Bulgaria"
      ]
    self.risk_tlds = [".ml", ".gq", ".tk", ".cf", ".su", ".cn", ".do", ".pw", ".cc", ".ng"]
    self.risk_registrars = [
      "Backorder Ltd", 
      "Harmon Web Global Service", 
      "HoganHost LTD", 
      "FE-SU",
      "FE-RU",
      "URL Solutions",
      "Nets To Limited",
      "Domainhosting.com.ng",
      "DDD TECHNOLOGY PTE. LTD",
      "Aceville Pte. Ltd."
      ]
  
  def is_valid_value(self, val) -> bool:
    return val not in (None, "")

  def clean_string(self, s: str) -> str:
    return re.sub(r'[^a-z\s]', '', s.lower().strip())

  def is_risk_measurement(self, val: str, risk_list: list) -> bool:
    if not self.is_valid_value(val):
        raise ValueError("Provided value is invalid")
    cleaned_val = self.clean_string(val)
    return any(cleaned_val in self.clean_string(element) for element in risk_list)

  def is_risk_country_measurement(self, val: str) -> bool:
    try:
        return self.is_risk_measurement(val, self.risk_countries)
    except ValueError as e:
        print(f"Error occurred: {e}")
        return False 

  def is_risk_tld_measurement(self, val: str) -> bool:
      try:
        return self.is_risk_measurement(val, self.risk_tlds)
      except ValueError as e:
        print(f"Error occurred: {e}")
        return False

  def is_risk_registrar_measurement(self, val: str) -> bool:
      try:
        return self.is_risk_measurement(val, self.risk_registrars)
      except ValueError as e:
        print(f"Error occurred: {e}")
        return False
  
    

  