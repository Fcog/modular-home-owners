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
        icon = 'uni52'
        template = 'base/blocks/hero.html'


class FrontPage(Page):
    # Database fields

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('person', HeroBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]