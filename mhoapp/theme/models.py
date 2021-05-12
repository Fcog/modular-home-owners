from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_link_block.blocks import LinkBlock

from mhoapp.base.utils import truncate_float, currency
from mhoapp.homes.models.StyleCategory import StyleCategory
from mhoapp.homes.models.PriceRanges import PriceRanges
from mhoapp.homes.models.HomePage import HomePage
from mhoapp.partners.models import LocationCategory, PartnerTypePage
from mhoapp.resources.models import ResourcePage
from mhoapp.base.models import BlocksSettings
from mhoapp.base.utils import remove_extension


class PartnersButtons(blocks.ChoiceBlock):
    choices = tuple(LocationCategory.objects.values_list('code','name'))

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        context['buttons'] = list(map(
            lambda item: {
                'hx_get': f'{item.url}?location={value}',
                'hx_target': '#ajax-response',
                'text': f'{value} {item.title}',
                'image': item.icon.url,
            },
            PartnerTypePage.objects.all()
        ))

        return context

    class Meta:
        label = 'Partners by State Buttons'
        icon = 'placeholder'
        template = 'patterns/organisms/partners-buttons/partners-buttons.html'


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


class BlueBoxCTA(blocks.StructBlock):
    title = blocks.CharBlock()
    text = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = LinkBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)    
        return context

    class Meta:
        label = 'Blue Box CTA'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/blue-box.html'


class ResourcesCTA(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])

        context['text'] = global_data.resources_text                
        context['links'] = ResourcePage.objects.live()
        context['links_list_class'] = "pt-16 md:pt-44"

        return context

    class Meta:
        label = 'Resources CTA'
        admin_text = 'This block is configured in the MHO settings page.'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/links-list.html'


class PartnersCTA(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])

        context['column_1_title'] = global_data.partner_1_title       
        context['column_1_text'] = global_data.partner_1_text     
        context['column_1_button_text'] = global_data.partner_1_button_text 
        context['column_1_button_url'] = global_data.partner_1_button_link.url     
        context['column_2_title'] = global_data.partner_2_title       
        context['column_2_text'] = global_data.partner_2_text        
        context['column_2_button_text'] = global_data.partner_2_button_text     
        context['column_2_button_url'] = global_data.partner_2_button_link.url                

        return context

    class Meta:
        label = 'Partners CTA'
        admin_text = 'This block is configured in the MHO settings page.'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/double-column.html'


class GetYourHouseCTA(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])

        context['title'] = global_data.gyh_title        
        context['column_1_title'] = global_data.gyh_column_1_title        
        context['column_1_text'] = global_data.gyh_column_1_text         
        context['column_2_title'] = global_data.gyh_column_2_title        
        context['column_2_text'] = global_data.gyh_column_2_text         
        context['column_3_title'] = global_data.gyh_column_3_title        
        context['column_3_text'] = global_data.gyh_column_3_text     
        context['link_1_text'] = global_data.gyh_link_1_text     
        context['link_1_url'] = global_data.gyh_link_1_link.url
        context['link_2_text'] = global_data.gyh_link_2_text     
        context['link_2_url'] = global_data.gyh_link_2_link.url

        return context

    class Meta:
        label = 'Get Your House CTA'
        icon = 'placeholder'
        admin_text = 'This block is configured in the MHO settings page.'
        template = 'patterns/organisms/cta/icons-cols.html'


class PopularHomesGrid(blocks.StructBlock):
    title = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = LinkBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)

        context['button_url'] = value['button_link'].get_url

        context['homes'] = HomePage.objects.live().order_by('-hit_count_generic__hits')[:6]

        context['homes_grid_class'] = "pb-20 md:pb-36"

        return context

    class Meta:
        label = 'Popular Homes Grid'
        icon = 'placeholder'
        template = 'patterns/organisms/homes-grid/homes-grid.html'


class ForumCTA(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])

        context['title'] = global_data.forum_title
        context['text'] = global_data.forum_text
        context['button_text'] = global_data.forum_button_text
        context['button_url'] = global_data.forum_button_url()

        return context

    class Meta:
        label = 'Forum CTA'
        icon = 'placeholder'
        admin_text = 'This block is configured in the MHO settings page.'
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
            StyleCategory.objects.all().order_by('name')
        ))
        context['price_ranges'] = list(map(
            lambda item: {
                'id': f'{item.get_type_display().lower()}-{item.price}',
                'text': f'{item.get_type_display()} ${item.price}',
                'url': item.homes_search_page.url if item.homes_search_page else ''
            },
            PriceRanges.objects.all().order_by('price')
        ))
        return context

    class Meta:
        label = 'Hero'
        icon = 'home'
        template = 'patterns/organisms/hero-home/hero-home.html'


class HeadingH1(blocks.StructBlock):
    title = blocks.CharBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context    

    class Meta:
        label = 'H1'
        icon = 'title'
        template = 'patterns/atoms/headings/h1.html'


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