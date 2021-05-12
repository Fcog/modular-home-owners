from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from mhoapp.theme.blocks import HeadingH2
from mhoapp.resources.models import ResourcePage


class ArticlesIndexPage(Page):
    template = 'patterns/templates/archive/archive.html'

    # Parent page / subpage type rules
    subpage_types = ['ArticlePage']


class ArticlePage(Page):
    template = 'patterns/templates/articles/single.html'

    # Database fields
    resource_category = models.ForeignKey(ResourcePage, on_delete=models.SET_NULL, null=True)

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
        FieldPanel('resource_category'),
        StreamFieldPanel('body'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['ArticlesIndexPage']
