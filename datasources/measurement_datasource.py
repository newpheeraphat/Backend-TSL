class Measurement: 
  def is_ssl_valid(self, ssl_valid: str) -> bool: 
    try:
      return ssl_valid == "Valid"
    except Exception as e: 
      print(f"Error occurred is_ssl_valid: {e}")
      return False
  
  def is_risk_country(self, country: str) -> bool: 
    try:
      safe_country = ['US', 'UK']
      if country in safe_country: 
        return True 
      return False
    except Exception as e: 
      print(f"Error occurred is_risk_country: {e}")
      return False
  
  def is_whois_hidden(self, is_hidden: str) -> bool:
    try:
      if is_hidden == 'protected':
        return True 
      return False
    except Exception as e: 
      print(f"Error occurred is_whois_hidden: {e}")
      return False
  
  def domain_age_seven_year(self, domain_age) -> bool: 
    try:
      return int(domain_age) > 7
    except Exception as e: 
      print(f"Error occurred domain_age_seven_year: {e}")
      return False
  
  def check_tranco_rank(self, rank) -> bool: 
    try: 
      if int(rank) < 500000: 
        return True 
      return False
    except Exception as e: 
      print(f"Error occurred check_tranco_rank: {e}")
      return False
  
  def is_paid_email(self, email) -> bool: 
    try: 
      free_email_domains = [
            "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", 
            "aol.com", "mail.com", "yandex.com", "protonmail.com"
        ]
      domain = email.split('@')[-1].lower()
      return domain not in free_email_domains
    except Exception as e: 
      print(f"Error occurred is_paid_email: {e}")
      return False
    

  