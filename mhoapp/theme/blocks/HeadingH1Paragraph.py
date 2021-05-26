from wagtail.core import blocks


class HeadingH1Paragraph(blocks.StructBlock):
    centered = blocks.BooleanBlock()      
    title = blocks.CharBlock()
    introduction = blocks.TextBlock(required=False, default="")
    
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context    

    class Meta:
        label = 'Heading H1 + Paragraph'
        icon = 'placeholder'
        template = 'patterns/molecules/headings/page/page.html'