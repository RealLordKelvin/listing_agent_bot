from django.core.management.base import BaseCommand, CommandError
from listings.models import Listing, User
from listings.scraper import scraper
from django.utils import timezone

class Command(BaseCommand):
    help = 'Scrape listings from a real estate agency'

    # def add_arguments(self, parser):
    #     parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        
        listings = scraper.execute_scraper()
        for listing in listings:
            if not listing:
                continue
            price = listing.get("price")
            reference_number = listing.get("reference_number")
            link = listing.get("link")
            user = User.objects.get(username="vincent")
            # If we dont't have this listng for given username and reference_number then..
            if not Listing.objects.filter(username=user, reference_number=reference_number).exists():
                Listing.objects.create(username=user,link=link, price=price, reference_number=reference_number)
                self.stdout.write(self.style.SUCCESS('Successfully imported "%s"' % reference_number))