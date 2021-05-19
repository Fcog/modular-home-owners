from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.embeds.blocks import EmbedBlock

from mhoapp.theme.blocks import HeadingH2
from mhoapp.resources.models import ResourcePage
from mhoapp.theme import blocks as custom_blocks


class ArticlesIndexPage(Page):
    template = 'patterns/templates/archive/archive.html'

    # Parent page / subpage type rules
    subpage_types = ['ArticlePage']


class ArticlePage(Page):
    template = 'patterns/templates/articles/single.html'

    # Database fields
    resource_category = models.ForeignKey(ResourcePage, on_delete=models.SET_NULL, null=True)

    body = StreamField([
        ('separator', custom_blocks.Separator()),
        ('headingH2', HeadingH2()),
        ('paragraph', custom_blocks.Paragraph()),
        ('image', custom_blocks.ImageCaption()),
        ('buttons', custom_blocks.Buttons()),
        ('quote', custom_blocks.GreenQuote()),
        ('quote2', custom_blocks.BlueQuote()),
        ('embed', EmbedBlock()),
    ], default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('resource_category'),
        StreamFieldPanel('body'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['ArticlesIndexPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['header_theme'] = 'green'
        context['header_show_title'] = True
        context['prev_article_title'] = f'Previous Topic: {self.get_prev_sibling().title}' if self.get_prev_sibling() else ''
        context['prev_article_url'] = self.get_prev_sibling().url if self.get_prev_sibling() else ''
        context['next_article_title'] = f'Next Topic: {self.get_next_sibling().title}' if self.get_next_sibling() else ''
        context['next_article_url'] = self.get_next_sibling().url if self.get_next_sibling() else ''        
        return context    
