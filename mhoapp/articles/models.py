from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from mhoapp.theme.models import HeadingH2

class ArticlesIndexPage(Page):
    template = 'patterns/pages/archive/archive.html'

    # Parent page / subpage type rules
    subpage_types = ['ArticlePage']


class ArticlePage(Page):
    template = 'patterns/pages/articles/single.html'

    # Database fields
    body = StreamField([
        ('headingH2', HeadingH2()),
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

    # Parent page / subpage type rules
    parent_page_types = ['ArticlesIndexPage']
