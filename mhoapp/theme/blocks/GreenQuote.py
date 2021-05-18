from wagtail.core import blocks


class GreenQuote(blocks.StructBlock):
    text = blocks.RichTextBlock(required=True)    

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context    

    class Meta:
        icon = 'openquote'
        label = 'Green Quote'
        template = 'patterns/molecules/quotes/green-quote.html'    