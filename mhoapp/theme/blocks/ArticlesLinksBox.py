from wagtail.core import blocks


class ArticlesLinksBox(blocks.StructBlock):
    title = blocks.CharBlock(default="Helpful Articles")
    links = blocks.ListBlock(blocks.PageChooserBlock(page_type="articles.ArticlePage"))

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context

    class Meta:
        label = 'Articles Links Box'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/green-box.html'