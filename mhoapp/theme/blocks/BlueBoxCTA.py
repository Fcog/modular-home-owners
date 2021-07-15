from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock


class BlueBoxCTA(blocks.StructBlock):
    layout = blocks.ChoiceBlock(choices=[
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical'),
    ], icon='title', default='horizontal') 
    title = blocks.RichTextBlock(features=['bold'])
    text = blocks.TextBlock()
    button_text = blocks.CharBlock()
    form_id = blocks.CharBlock()
    form_height = blocks.CharBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context

    class Meta:
        label = 'Blue Box CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/blue-box.html'