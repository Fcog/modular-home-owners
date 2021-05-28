from django import forms
from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail_multi_upload.edit_handlers import MultipleImagesPanel

from .LocationCategory import LocationCategory
from mhoapp.theme import blocks as custom_blocks
from mhoapp.base.models import HomeSearchPageSettings


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
        ('buttons', custom_blocks.Buttons()),
        ('image', custom_blocks.ImageCaption()),
        ('embed', EmbedBlock()),
    ], default='')

    bottom_content = StreamField([
        ('separator', custom_blocks.Separator()),
        ('headingH2', custom_blocks.HeadingH2()),
        ('ResourcesCTA', custom_blocks.ResourcesCTA()),
        ('PartnersCTA', custom_blocks.PartnersCTA()),
        ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
        ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
        ('articlesCTA', custom_blocks.ArticlesCTABlock()),
        ('ForumCTA', custom_blocks.ForumCTA()),
        ('paragraph', custom_blocks.ParagraphSection()),
        ('form', custom_blocks.FormBlock()),
        ('quote', custom_blocks.GreenQuote()),
        ('quote2', custom_blocks.BlueQuote()),
        ('image', custom_blocks.ImageCaption()),
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
                MultipleImagesPanel(
                    'gallery_images',
                    label="Image Gallery",
                    image_field_name="image"
                ),
            ],
            heading="Images",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [     
                StreamFieldPanel('left_content'),
            ],
            heading="Left side content",
            classname="collapsible collapsed"
        ),                   
        MultiFieldPanel(
            [     
                StreamFieldPanel('bottom_content'),
            ],
            heading="Bottom content",
            classname="collapsible collapsed"
        ),         
    ]

    # Parent page / subpage type rules
    parent_page_types = ['PartnerTypePage']    

    def PartnerType(self):
        return self.get_parent()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        global_data = HomeSearchPageSettings.for_request(request)          

        context['homes_search_page_url'] = f'{global_data.homes_search_page.full_url}?partner={self.slug}' if global_data.homes_search_page else ''

        return context



