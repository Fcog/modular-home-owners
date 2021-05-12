from wagtail.core import blocks


class HeadingH2(blocks.StructBlock):
    title = blocks.RichTextBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context    

    class Meta:
        label = 'H2'
        icon = 'title'
        template = 'patterns/atoms/headings/h2.html'

