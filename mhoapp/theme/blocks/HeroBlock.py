from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_link_block.blocks import LinkBlock

from mhoapp.homes.models.StyleCategory import StyleCategory
from mhoapp.homes.models.PriceRanges import PriceRanges


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    introduction = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    search_button_text = blocks.CharBlock(default='Search Homes')
    filter_bar_text = blocks.CharBlock(default='')
    links = blocks.ListBlock(blocks.StructBlock([
        ('text', blocks.CharBlock()),
        ('link', LinkBlock()),
    ]))

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        context['styles'] = list(map(
            lambda item: {
                'id': item.name.lower(),
                'text': item.name,
                'custom_data': item.style_page.url if item.style_page else ''
            },
            StyleCategory.objects.all().order_by('name')
        ))
        context['price_ranges'] = list(map(
            lambda item: {
                'id': f'{item.get_type_display().lower()}-{item.price}',
                'text': f'{item.get_type_display() if item.get_type_display() == "Under" else ""} ${"{:,}".format(item.price)} {"+" if item.get_type_display() == "Over" else ""}',
                'custom_data': item.homes_search_page.url if item.homes_search_page else ''
            },
            PriceRanges.objects.all().order_by('price')
        ))
        return context

    class Meta:
        label = 'Hero'
        icon = 'home'
        template = 'patterns/organisms/hero-home/hero-home.html'

