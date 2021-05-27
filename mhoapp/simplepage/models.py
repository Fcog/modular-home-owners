from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, TabbedInterface, ObjectList
from wagtail.embeds.blocks import EmbedBlock
from wagtailyoast.edit_handlers import YoastPanel

from mhoapp.theme import blocks as custom_blocks

# Create your models here.
class SimplePage(Page):
    template = 'patterns/templates/articles/single.html'

    keywords = models.CharField(default='', blank=True, max_length=100)

    # Database fields
    body = StreamField([
        ('headingH2', custom_blocks.HeadingH2()),
        ('paragraph', custom_blocks.Paragraph()),        
        ('image', custom_blocks.ImageCaption()),
        ('buttons', custom_blocks.Buttons()),
        ('quote', custom_blocks.GreenQuote()),
        ('quote2', custom_blocks.BlueQuote()),
        ('embed', EmbedBlock()),
        ('separator', custom_blocks.Separator()),
    ], default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promotion')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])    

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['header_theme'] = 'green'
        context['header_show_title'] = True
        return context        

    class Meta:
        verbose_name = "One column page (Blue header)"        