from bs4 import BeautifulSoup
import requests

def get_search_page(url):
    r = requests.get(url)
    page = BeautifulSoup(r.content, 'html5lib') 
    return page 