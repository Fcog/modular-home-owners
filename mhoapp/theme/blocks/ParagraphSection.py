from wagtail.core import blocks


class ParagraphSection(blocks.StructBlock):
    paragraph = blocks.RichTextBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context    

    class Meta:
        label = 'Paragraph'
        icon = 'doc-full'
        template = 'patterns/molecules/paragraphs/paragraph.html'    