from agencies import first_mallorca
from  helpers import scraping

URL_FIRST_MALLORCA = "https://www.firstmallorca.com/en/search"

page = scraping.get_search_page(URL_FIRST_MALLORCA)

listings = first_mallorca.first_mallorca_scraper(page)

print(listings)