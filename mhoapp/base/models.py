from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from mhoapp.theme.models import *


class HeroBlock(blocks.StructBlock):
    # Database fields

    title = blocks.CharBlock()
    background_image = ImageChooserBlock()

    class Meta:
        icon = 'placeholder'
        template = 'blocks/hero.html'


class FrontPage(Page):
    template = 'patterns/pages/front_page.html'
    
    # Database fields

    body = StreamField([
        ('hero', HeroBlock()),
        ('section', SectionBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    # Parent page / subpage type rules

    parent_page_types = []  # Frontpage is created only on the root.


