from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_link_block.blocks import LinkBlock

from mhoapp.homes.models import StyleCategory, PriceRanges, HomePage
from mhoapp.base.models import MHOSettings


class GetYourHouseCTA(blocks.StructBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = MHOSettings.objects.first()

        context['title'] = global_data.gyh_title        
        context['column_1_title'] = global_data.gyh_column_1_title        
        context['column_1_text'] = global_data.gyh_column_1_text         
        context['column_2_title'] = global_data.gyh_column_2_title        
        context['column_2_text'] = global_data.gyh_column_2_text         
        context['column_3_title'] = global_data.gyh_column_3_title        
        context['column_3_text'] = global_data.gyh_column_3_text     
        context['link_1_text'] = global_data.gyh_link_1_text     
        context['link_1_link'] = global_data.gyh_link_1_link     
        context['link_2_text'] = global_data.gyh_link_2_text     
        context['link_2_link'] = global_data.gyh_link_2_link     

        return context

    class Meta:
        label = 'Get Your House CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/icons-cols.html'


class PopularHomesGrid(blocks.StructBlock):
    title = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = LinkBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)

        context['homes'] = HomePage.objects.live().order_by('-hit_count_generic__hits')[:6]

        return context

    class Meta:
        label = 'Popular Homes Grid'
        icon = 'placeholder'
        template = 'patterns/organisms/homes-grid/homes-grid.html'


class ForumCTA(blocks.StructBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = MHOSettings.objects.first()

        context['title'] = global_data.forum_title
        context['text'] = global_data.forum_text
        context['button_text'] = global_data.forum_button_text
        context['button_link'] = global_data.forum_button_url()

        return context

    class Meta:
        label = 'Forum CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/cta.html'


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


class HeroBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    introduction = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    search_button_text = blocks.CharBlock(default='Search Homes')
    filter_bar_text = blocks.CharBlock(default='')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
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
