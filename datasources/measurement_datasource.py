from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class Measurement: 
  def extract_data_from_url_selenium(self, url: str): 
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--disable-gpu") 
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    try: 
      driver.get(url)
      html_content = driver.page_source
      soup = BeautifulSoup(html_content, 'html.parser')
      element = soup.find_all("span", class_="subtitle")
      return element
    except Exception as e: 
      print("Error Occurred: " + e)
      return;
    
  def is_risk(self, val: str, url: str) -> bool: 
    try:
      if (val == ""): raise Exception("Value is None")
      
      span_elements = self.extract_data_from_url_selenium(url)
      
      print(span_elements)
      
      risk_elements = [element.text for element in span_elements]
      
      return any(val.lower() in elements.lower() for elements in risk_elements)
    except Exception as e: 
      print(f"Error occurred is_risk_country: {e}")
      return True
    
  
    

  