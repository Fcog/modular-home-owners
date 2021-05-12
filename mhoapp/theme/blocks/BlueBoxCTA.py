from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock


class BlueBoxCTA(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = LinkBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)    
        return context

    class Meta:
        label = 'Blue Box CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/blue-box.html'

