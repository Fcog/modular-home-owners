from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from mhoapp.homes.models.HomePage import HomePage


class FloorplanGalleryImage(Orderable):
    # Database fields
    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='floorplan_gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        null=True,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    # Editor panels configuration
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]