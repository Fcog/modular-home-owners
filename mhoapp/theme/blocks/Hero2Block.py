from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from mhoapp.homes.models.StyleCategory import StyleCategory
from mhoapp.homes.models.PriceRanges import PriceRanges


class Hero2Block(blocks.StructBlock):
    title = blocks.CharBlock()
    introduction = blocks.TextBlock()
    image = ImageChooserBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        context['heading'] = value['title']
        return context

    class Meta:
        label = 'Hero 2'
        icon = 'home'
        template = 'patterns/organisms/hero2/hero2.html'

