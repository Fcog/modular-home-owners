from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from mhoapp.homes.models.StyleCategory import StyleCategory
from mhoapp.homes.models.PriceRanges import PriceRanges


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    introduction = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    search_button_text = blocks.CharBlock(default='Search Homes')
    filter_bar_text = blocks.CharBlock(default='')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        context['styles'] = list(map(
            lambda item: {
                'id': item.name.lower(),
                'text': item.name,
            },
            StyleCategory.objects.all().order_by('name')
        ))
        context['price_ranges'] = list(map(
            lambda item: {
                'id': f'{item.get_type_display().lower()}-{item.price}',
                'text': f'{item.get_type_display()} ${item.price}',
                'url': item.homes_search_page.url if item.homes_search_page else ''
            },
            PriceRanges.objects.all().order_by('price')
        ))
        return context

    class Meta:
        label = 'Hero'
        icon = 'home'
        template = 'patterns/organisms/hero-home/hero-home.html'

