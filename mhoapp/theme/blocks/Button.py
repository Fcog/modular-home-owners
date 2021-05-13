from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock


class Button(blocks.StructBlock):
    text = blocks.CharBlock()
    link = LinkBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        context['url'] = value['link'].get_url
        context['size'] = 'small'
        context['text_size'] = 'small'
        context['color'] = 'blue'
        context['inverted'] = False
        return context    

    class Meta:
        label = 'Button'
        icon = 'radio-full'
        template = 'patterns/atoms/button/button.html'