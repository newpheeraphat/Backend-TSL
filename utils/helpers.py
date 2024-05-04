import requests
import metadata_parser
from urllib.parse import urlparse, urlunparse

def get_domain_name(url): 
    if ("https://" in url) or ("http://" in url):
        parsed_url = urlparse(url)
        domain_name = parsed_url.netloc
        if domain_name.startswith("www."):
            domain_name = domain_name[4:]
        return domain_name
    elif url.startswith("www."):
        return url[4:]
    else:
        return url

def redirect_to_homepage(url):
    parsed_url = urlparse(url)
    homepage_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    has_homepage = requests.get(homepage_url)

    if has_homepage:
        return homepage_url
    return url


def make_request(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  
    try:
        return url
    except requests.ConnectionError:
        try:
            url = 'https://' + url.split('http://')[1]
            return url
        except requests.ConnectionError as e:
            return f"Failed to make a request: {e}"
        
def preprocessing_url_detection(url):
    try:
        for i in range(len(url) - 1, -1, -1):
            if url[i] == "/":
                url = url[:i]
            else:
                return url
    except Exception as e: 
        print(f"Failed to proprocessing url {url}: {e}")
        return None
        
        
def get_tag_information(url):
    return metadata_parser.MetadataParser(url)