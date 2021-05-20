from django.apps import apps
from wagtail.core import blocks
from wagtailsvg.blocks import SvgChooserBlock

class IconCard(blocks.StructBlock):
    text = blocks.CharBlock(required=True)
    icon = SvgChooserBlock(required=True)


class IconsGrid(blocks.StructBlock):
    cards = blocks.ListBlock(IconCard())

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context

    class Meta:
        label = 'Icons Grid'
        icon = 'placeholder'
        template = 'patterns/molecules/icons-grid/icons-grid.html'
       
