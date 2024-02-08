from datasources.company_datasource import Company
from datasources.owner_datasource import Owner
from datasources.registrar_datasource import Registrar
from datasources.websitedata_datasource import WebsiteData
from datasources.server_datasource import Server
from datasources.measurement_datasource import Measurement
from utils.helpers import *



def run(raw_url):
    url = preprocessing_url(raw_url)
    server = Server(url)
    company = Company(url)
    website = WebsiteData(url)
    owner = Owner(url)
    registrar = Registrar(url)
    measurement = Measurement()
    
    # Measurement
    ssl_valid = website.check_ssl_certificate()
    is_hidden = website.is_whois_hidden()
    country = owner.get_country()
    email = registrar.get_email()
    domain_age = website.get_domain_age()
    tranco_rank = website.get_tranco_rank()

    response_data = {
      'server': {
        "name": server.get_server_name()
      },
      'company': {
        'organization': company.get_company_data()['Organization'],
        'owner': company.get_company_data()['Owner'],
        'address': company.get_company_data()['Address'],
        'country': company.get_company_data()['Country'],
        'email': company.get_company_data()['Contact Email']
      },
      'website_data': {
        # 'rank': website.get_alexa_rank(),
        "tranco_rank": tranco_rank,
        'ip': website.get_ip_address(),
        'status_code': website.get_status_code(),
        'domain_age': domain_age,
        'ssl_valid': ssl_valid,
        'ssl_type': website.get_certificate_type(),
        'whois_register_date': website.get_whois_registration_date(),
        'whois_last_update_date': website.get_whois_last_updated(),
        'whois_renew_date': website.get_whois_last_updated(),
        'redirect_domain': website.get_redirected_domains(),
        'is_hidden': is_hidden
      },
      'owner': {
        'organization': owner.get_organization_name(),
        'ca': owner.get_CA(),
        'country': country
      },
      'registrar': {
        'domain': registrar.get_domain_registrar(),
        'iana_id': registrar.get_iana_id(),
        'email': email
      },
      'measurement': {
        'is_ssl_valid': measurement.is_ssl_valid(ssl_valid),
        "is_whois_show": measurement.is_whois_hidden(is_hidden),
        "is_risk_country": measurement.is_risk_country(country),
        "is_paid_email": measurement.is_paid_email(email),
        "is_age_more_seven_year": measurement.domain_age_seven_year(domain_age),
        "tranco_rank": measurement.check_tranco_rank(tranco_rank)
      }
    }
    
    return response_data
