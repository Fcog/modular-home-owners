from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from mhoapp.theme.models import *

class FlexibleOneColumnPage(Page):
    template = 'patterns/pages/flexible/one-col.html'

    # Database fields

    body = StreamField([
        ('headingH1', HeadingH1()),
        ('headingH2', HeadingH2()),
        ('resourcesCTA', ResourcesCTABlock()),
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


class FlexibleTwoColumnPage(Page):
    template = 'patterns/pages/flexible/two-col.html'
