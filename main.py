import requests
from bs4 import BeautifulSoup
import json

def statusCode(site_url):
    response = requests.get(site_url);
    return response

