from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from mhoapp.homes.models import StyleCategory, PriceRanges


class ResourcesCTABlock(blocks.StructBlock):
    WHITE = 'WH'
    BLUE = 'BL'

    style = blocks.ChoiceBlock(
        choices=[
            (WHITE, 'white'),
            (BLUE, 'blue'),
        ],
        default=WHITE,
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
    filter_bar_text = blocks.CharBlock(default='')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['heading'] = value['heading']
        context['introduction'] = value['introduction']
        context['image'] = value['image']
        context['search_button_text'] = value['search_button_text']
        context['filter_bar_text'] = value['filter_bar_text']
        context['styles'] = list(map(
            lambda item: {
                'id': item.name.lower(),
                'text': item.name,
            },
            StyleCategory.objects.all()
        ))
        context['price_ranges'] = list(map(
            lambda item: {
                'id': f'{item.get_type_display().lower()}-{item.price}',
                'text': f'{item.get_type_display()} ${item.price}',
            },
            PriceRanges.objects.all()
        ))
        return context

    class Meta:
        label = 'Hero'
        icon = 'home'
        template = 'patterns/organisms/hero-home/hero-home.html'


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
