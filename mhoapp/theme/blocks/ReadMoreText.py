from wagtail.core import blocks


class ReadMoreText(blocks.StructBlock):
    text_size = blocks.ChoiceBlock(choices=[
        ('small', 'Small'),
        ('normal', 'Normal'),
    ], icon='title', default='normal')      
    paragraph = blocks.RichTextBlock(default='')    

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)    
        return context

    class Meta:
        label = 'Read More text'
        icon = 'placeholder'
        template = 'patterns/molecules/paragraphs/readmore.html'

