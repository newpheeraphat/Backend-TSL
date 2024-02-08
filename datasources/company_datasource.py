import whois

class Company:
  def __init__(self, url: str) -> None: 
    self.url = url
    
  def get_company_data(self):
    try:
      domain_info = whois.whois(self.url)
      
      data = {
          "Organization": domain_info.get("org", "N/A"),
          "Address": domain_info.get("address", "N/A"),
          "Contact Email": domain_info.get("email", "N/A"),
          "Country": domain_info.get("country", "N/A"),
          "Owner": domain_info.get("registrar", "N/A")
      }
      return data
    except whois.parser.PywhoisError as e:
      return f"An error occurred: {e}"
  