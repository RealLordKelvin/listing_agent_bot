def first_mallorca_scraper(page_object):
    properties_cards = get_properties(page_object)
    listings = get_informations_of_properties(properties_cards)
    return listings


def get_properties(initial_search_page):
    
    properties_cards = initial_search_page.find('div', attrs = {'class':'area'})
    if not properties_cards:
        raise Exception('No properties card found')
    return properties_cards

def get_informations_of_properties(properties_cards):

    listings = []
    for _property in properties_cards.findAll('div', attrs = {'class':'card'}):
        # Für jede gelistete property auf der ersten Seite der search Ergebnisse gucken wir auf den...
        # ... quick card...
        quick = _property.find('div', attrs = {'class':'quick'})
        # ... und auf die description card und suchen nach...
        description = _property.find('div', attrs = {'class':'description'})
        listing = {}
        try:
            # ... der reference nummer...
            listing['reference_number'] = description.find('div', attrs = {'class':'ref_id'}).get_text()
            # ... der listing preis...
            listing['price'] = quick.find('div', attrs = {'class':'currency'}).get_text()
            # ... und den link zu der Seite...
            link = description.find('a').get('href')
            listing['link'] = f"https://www.firstmallorca.com{link}"
        except:
            pass
        
        listings.append(listing)

    return listings

