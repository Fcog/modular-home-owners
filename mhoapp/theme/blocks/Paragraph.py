from wagtail.core import blocks


class Paragraph(blocks.StructBlock):
    text_size = blocks.ChoiceBlock(choices=[
        ('small', 'Small'),
        ('normal', 'Normal'),
    ], icon='title', default='normal')  
    paragraph = blocks.RichTextBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context    

    class Meta:
        icon = 'doc-full'
        template = 'patterns/atoms/paragraph/paragraph.html'    