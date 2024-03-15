import requests
import metadata_parser
from urllib.parse import urlparse

def remove_www(url: str) -> str:
    if url[0:3] == "www":
        return url[4:]
    return url

def get_domain_name(url): 
    if ("https://" in url) or ("http://" in url):
        parsed_url = urlparse(url)
        domain_name = parsed_url.netloc
        return domain_name
    elif url[0:3] == "www":
        return url[4:]
    else:
        return url

def make_request(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Default to HTTP if no scheme is provided
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