import socket
import requests
from utils.helpers import *

class Server:
    def __init__(self, url: str) -> None: 
        self.url = url
        self.web = make_request(self.url)
        self.response = requests.get(self.web)
        
    def get_server_name(self):
        try:
            response = requests.get(self.web)
            server = response.headers.get('Server')
            return server if server else "Server name not found."
        except requests.RequestException as e:
            return f"An error occurred: {e}"

    def print_url(self) -> None: 
        print(self.url)
