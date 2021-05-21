from django.apps import apps
from wagtail.core import blocks
from wagtailsvg.blocks import SvgChooserBlock
from wagtail_link_block.blocks import LinkBlock


class ThreeColumnsBlock(blocks.StructBlock):
    columns = blocks.ListBlock(blocks.StructBlock([
        ('icon', SvgChooserBlock(required=True)),
        ('title', blocks.CharBlock(required=True)),
        ('text', blocks.TextBlock(required=True)),
        ('link_text', blocks.CharBlock()),
        ('link', LinkBlock()),
    ]))    

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context

    class Meta:
        label = 'Three Column Blocks'
        icon = 'placeholder'
        template = 'patterns/organisms/columns/three-blocks.html'