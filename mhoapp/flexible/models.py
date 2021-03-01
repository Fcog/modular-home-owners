from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class FlexibleOneColumnPage(Page):
    template = 'patterns/pages/flexible/one-col.html'

    # Database fields

    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('text', blocks.TextBlock()),
        ('char', blocks.CharBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], default='')

    # Editor panels configuration

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class FlexibleTwoColumnPage(Page):
    template = 'patterns/pages/flexible/two-col.html'
