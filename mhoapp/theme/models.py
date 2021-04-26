from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from mhoapp.homes.models import StyleCategory, PriceRanges

class ResourcesCTABlock(blocks.StructBlock):
    WHITE = 'WH'
    BLUE = 'BL'

    style = blocks.ChoiceBlock(
        choices=[
            (WHITE, 'white'),
            (BLUE, 'blue'),
        ],
        default=WHITE,
    )

    class Meta:
        label = 'Resources CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/text-links-button/text-links-button.html'


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
    button_link = blocks.PageChooserBlock(required=False)
    button_text = blocks.CharBlock()

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

        return context
    
    class Meta:
        label = 'Articles CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/text-links-button/text-links-button.html'        


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    introduction = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    search_button_text = blocks.CharBlock(default='Search Homes')
    filter_bar_text = blocks.CharBlock(default='')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['heading'] = value['heading']
        context['introduction'] = value['introduction']
        context['image'] = value['image']
        context['search_button_text'] = value['search_button_text']
        context['filter_bar_text'] = value['filter_bar_text']
        context['styles'] = list(map(
            lambda item: {
                'id': item.name.lower(),
                'text': item.name,
            },
            StyleCategory.objects.all()
        ))
        context['price_ranges'] = list(map(
            lambda item: {
                'id': f'{item.get_type_display().lower()}-{item.price}',
                'text': f'{item.get_type_display()} ${item.price}',
            },
            PriceRanges.objects.all()
        ))
        return context

    class Meta:
        label = 'Hero'
        icon = 'home'
        template = 'patterns/organisms/hero-home/hero-home.html'


class HeadingH1(blocks.CharBlock):
    class Meta:
        label = 'H1'
        icon = 'title'
        template = 'patterns/atoms/headings/h1.html'


class HeadingH2(blocks.CharBlock):
    class Meta:
        label = 'H2'
        icon = 'title'
        template = 'patterns/atoms/headings/h2.html'
