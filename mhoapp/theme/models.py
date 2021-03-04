from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ResourcesCTABlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(
        choices=[
            ('WHITE', 'white'),
            ('BLUE', 'blue'),
        ],
    )

    class Meta:
        label = 'Resources CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/text-links-button/text-links-button.html'


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    introduction = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    search_button_text = blocks.CharBlock(default='Search Homes')

    class Meta:
        label = 'Hero'
        icon = 'home'
        template = 'patterns/organisms/hero/hero.html'


class HeadingH1(blocks.CharBlock):
    class Meta:
        label = 'H1'
        icon = 'title'
        template = 'patterns/atoms/headings/h1.html'


class HeadingH2(blocks.CharBlock):
    class Meta:
        label = 'H2'
        icon = 'title'
        template = 'patterns/atoms/headings/h2.html'