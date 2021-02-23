from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    background_image = ImageChooserBlock()

    class Meta:
        icon = 'placeholder'
        template = 'base/blocks/hero.html'


class FrontPage(Page):
    # Database fields

    body = StreamField([
        ('hero', HeroBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]