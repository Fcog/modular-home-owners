from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock


class Buttons(blocks.StructBlock):
    links = blocks.ListBlock(blocks.StructBlock([
        ('text', blocks.CharBlock()),
        ('link', LinkBlock()),
    ]))

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)

        context['buttons'] = list(map(
            lambda item: {
                'url': item['link'].get_url,
                'text': item['text'],
                'size': 'small',
                'color': 'blue',
                'inverted': False,
                'text_size': 'small',
            },
            value['links']
        ))

        return context    

    class Meta:
        label = 'Buttons'
        icon = 'radio-full'
        template = 'patterns/molecules/buttons-list/buttons-list.html'