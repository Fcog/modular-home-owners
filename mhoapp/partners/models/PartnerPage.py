from django import forms
from django.db import models
from wagtail.core.models import Page
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .LocationCategory import LocationCategory


class PartnerPage(Page):
    template = 'patterns/templates/partners/partner-page.html'

    # Database fields
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    phone = models.TextField(max_length=25)
    website = models.URLField()
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    locations = ParentalManyToManyField(LocationCategory)

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('phone'),
                        FieldPanel('website'),
                    ]
                ),
            ],
            heading="Basic info",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('locations', widget=forms.CheckboxSelectMultiple),
            ],
            heading="Locations",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel('logo'),
                ImageChooserPanel('main_image'),
                InlinePanel(
                    'gallery_images',
                    label="Image Gallery"
                ),
            ],
            heading="Images",
            classname="collapsible collapsed"
        ),
    ]

    def PartnerType(self):
        return self.get_parent()

    # Parent page / subpage type rules
    parent_page_types = ['PartnerTypePage']

