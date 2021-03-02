from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class MHOSettings(models.Model):

    # Database fields

    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    logo_white = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contact_email = models.EmailField(max_length=255, default="services@mho.com")
    search_button_text = models.CharField(max_length=254, default="Find Your Home")

    # Editor panels configuration

    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('logo_white'),
        FieldPanel('contact_email'),
        FieldPanel('search_button_text'),
    ]

    def __str__(self):
        return "MHO website settings"
