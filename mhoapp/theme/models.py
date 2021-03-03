from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ResourcesCTABlock(blocks.StreamBlock):

    style = blocks.ChoiceBlock(
        choices=[
            ('WHITE', 'white'),
            ('BLUE', 'blue'),
        ],
    )

    class Meta:
        label = 'Resources CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/sections/text-links-button.html'


class HeadingH1(blocks.CharBlock):
    class Meta:
        label = 'H1 Heading'
        template = 'patterns/atoms/headings/h1.html'


class HeadingH2(blocks.CharBlock):
    class Meta:
        label = 'H2 Heading'
        template = 'patterns/atoms/headings/h2.html'