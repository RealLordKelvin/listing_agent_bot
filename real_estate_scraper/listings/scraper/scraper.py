from listings.scraper.agencies import first_mallorca
from  listings.scraper.helpers import scraping


def execute_scraper():

    URL_FIRST_MALLORCA = "https://www.firstmallorca.com/en/search"

    # First look at the initial search page.
    page = scraping.get_search_page(URL_FIRST_MALLORCA)
    # Find out, how many pages there are in total.
    number_of_pages = get_number_of_pages(page)
    # Now iterate over this number by changing also the search page index.
    listing_collection = []
    for page in range(number_of_pages):
        URL_FIRST_MALLORCA = "https://www.firstmallorca.com/en/search"
        if not page == 0:
            URL_FIRST_MALLORCA = f"{URL_FIRST_MALLORCA}/{page}" 
        target_page = scraping.get_search_page(URL_FIRST_MALLORCA)
        listings_for_page = first_mallorca.first_mallorca_scraper(target_page)
        listing_collection.append(listings_for_page)
        print(f"page {page} succesfull scraped")

    return [listing for listing_page in listing_collection for listing in listing_page]

# TODO make it dynamic depending on which site we are looking
def get_number_of_pages(initial_search_page)-> int:
        pagination_section = initial_search_page.find('section', attrs = {'class':'pagination'})
        # Look for: "of xx" in the pagination section.
        tag_number_of_pages_str = pagination_section.find("div", string=lambda x: x and x.startswith('of'))
        if not pagination_section:
            raise ValueError("No pagination section found")
        # We get for example: "of 73" --> of, 73 --> [1] == 73
        number_of_pages_str = tag_number_of_pages_str.get_text().split(" ")[1]

        return int(number_of_pages_str)