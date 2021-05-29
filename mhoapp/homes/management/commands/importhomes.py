import csv
from django.core.management.base import BaseCommand
from wagtail.core.models import Page
from wagtail.images.models import Image

from mhoapp.homes.models import HomesIndexPage, HomePage, StyleCategory
from mhoapp.partners.models import PartnerPage

class Command(BaseCommand):
    help = "Imports homes data from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument('homes_index_id', type=int)

    def handle(self, *args, **options):
        # delete existing homes pages
        HomePage.objects.all().delete()

        # Get the homes index page
        homesIndex = Page.objects.get(id=options['homes_index_id'])

        # import home pages
        reader = csv.DictReader(open(options['csv_file']))
        for row in reader:
            home_page = HomePage(
                title=row["home_name"],
                code=row["code"],
                sqft=row["sqft"],
                bedrooms=row["bedrooms"],
                baths=row["baths"],
                stories=row["stories"],
                cost=row["cost"],
                estimated_cost=row["estimatedCost"],
                link=row["link"],
                floorplans_link=row["floorplans"],
                info=row["info"],
                partner=PartnerPage.objects.get(id=int(row["manu_django_id"])),
                style=StyleCategory.objects.get(id=int(row["style_django_id"]))
            )

            if self.get_all_elevations(row["code"]):
                home_page.main_image = self.get_all_elevations(row["code"])[0]

            homesIndex.add_child(instance=home_page)
            home_page.save_revision().publish()
            print("published home page " + row["home_name"])

    def get_all_elevations(self, code):
        images = Image.objects.filter(title__startswith=code)
        return images