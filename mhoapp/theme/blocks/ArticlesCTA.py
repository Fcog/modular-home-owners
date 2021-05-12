from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock


class ArticlesCTABlock(blocks.StructBlock):
    introduction = blocks.RichTextBlock(features=['bold'])
    column_1_title = blocks.CharBlock()
    column_1_article_1 = blocks.PageChooserBlock(page_type='articles.ArticlePage')
    column_1_article_2 = blocks.PageChooserBlock(page_type='articles.ArticlePage', required=False)
    column_1_article_3 = blocks.PageChooserBlock(page_type='articles.ArticlePage', required=False)
    column_1_article_4 = blocks.PageChooserBlock(page_type='articles.ArticlePage', required=False)
    column_2_title = blocks.CharBlock()
    column_2_article_1 = blocks.PageChooserBlock(page_type='articles.ArticlePage', required=False)
    column_2_article_2 = blocks.PageChooserBlock(page_type='articles.ArticlePage', required=False)
    column_2_article_3 = blocks.PageChooserBlock(page_type='articles.ArticlePage', required=False)
    column_2_article_4 = blocks.PageChooserBlock(page_type='articles.ArticlePage', required=False)
    button_text = blocks.CharBlock()
    button_link = LinkBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        context['links_col_1'] = [
            value['column_1_article_1'],
            value['column_1_article_2'],
            value['column_1_article_3'],
            value['column_1_article_4'],
        ]
        context['links_col_2'] = [
            value['column_2_article_1'],
            value['column_2_article_2'],
            value['column_2_article_3'],
            value['column_2_article_4'],
        ]
        context['button_link'] = value['button_link']

        return context
    
    class Meta:
        label = 'Articles CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/text-links-button/text-links-button.html' 