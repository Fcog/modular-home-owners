from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailyoast.edit_handlers import YoastPanel

from mhoapp.theme.models import *


class FlexibleOneColumnPage(Page):
    template = 'patterns/templates/flexible/one-col.html'

    keywords = models.CharField(default='', blank=True, max_length=100)

    # Database fields
    body = StreamField([
        ('headingH1', HeadingH1()),
        ('headingH2', HeadingH2()),
        ('ResourcesCTA', ResourcesCTA()),
        ('PartnersCTA', PartnersCTA()),
        ('PopularHomesGrid', PopularHomesGrid()),
        ('GetYourHouseCTA', GetYourHouseCTA()),
        ('articlesCTA', ArticlesCTABlock()),
        ('ForumCTA', ForumCTA()),
        ('hero', HeroBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('text', blocks.TextBlock()),
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