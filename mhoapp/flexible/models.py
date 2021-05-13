from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailyoast.edit_handlers import YoastPanel

from mhoapp.theme import blocks as custom_blocks


class FlexibleOneColumnPage(Page):
    template = 'patterns/templates/flexible/one-col.html'

    keywords = models.CharField(default='', blank=True, max_length=100)

    # Database fields
    body = StreamField([
        ('separator', custom_blocks.Separator()),
        ('headingH1', custom_blocks.HeadingH1()),
        ('headingH2', custom_blocks.HeadingH2()),
        ('ResourcesCTA', custom_blocks.ResourcesCTA()),
        ('PartnersCTA', custom_blocks.PartnersCTA()),
        ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
        ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
        ('articlesCTA', custom_blocks.ArticlesCTABlock()),
        ('ForumCTA', custom_blocks.ForumCTA()),
        ('hero', custom_blocks.HeroBlock()),
        ('paragraph', custom_blocks.Paragraph()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promotion')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])