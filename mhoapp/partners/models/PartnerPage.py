from django import forms
from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from .LocationCategory import LocationCategory
from mhoapp.theme import blocks as custom_blocks


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
    locations = ParentalManyToManyField(LocationCategory)

    left_content = StreamField([
        ('headingH1', custom_blocks.HeadingH1()),
        ('headingH2', custom_blocks.HeadingH2()),
        ('paragraph', custom_blocks.Paragraph()),
        ('button', custom_blocks.Button()),
        ('Separator', custom_blocks.Separator()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], default='')

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
                InlinePanel(
                    'gallery_images',
                    label="Image Gallery"
                ),
            ],
            heading="Images",
            classname="collapsible collapsed"
        ),
        StreamFieldPanel('left_content'),
    ]

    def PartnerType(self):
        return self.get_parent()

    # Parent page / subpage type rules
    parent_page_types = ['PartnerTypePage']

