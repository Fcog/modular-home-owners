from django.db import models
from wagtail.core import blocks, fields 
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel, FieldRowPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel

from mhoapp.theme import blocks as custom_blocks


blocks = [
    ('Separator', custom_blocks.Separator()),
    ('headingH2', custom_blocks.HeadingH2()),
    ('ResourcesCards', custom_blocks.ResourcesCards()),
    ('ResourcesCTA', custom_blocks.ResourcesCTA()),
    ('PartnersCTA', custom_blocks.PartnersCTA()),
    ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
    ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
    ('articlesCTA', custom_blocks.ArticlesCTABlock()),
    ('articlesCTAGlobal', custom_blocks.ArticlesCTAGlobal()),
    ('ForumCTA', custom_blocks.ForumCTA()),
    ('paragraphSection', custom_blocks.ParagraphSection()),
    ('buttons', custom_blocks.Buttons()),
    ('quote', custom_blocks.GreenQuote()),
    ('quote2', custom_blocks.BlueQuote()),
    ('image', custom_blocks.ImageCaption()),
    ('embed', EmbedBlock()),
 ]

class ResourcesIndexPage(Page):
    template = 'patterns/templates/resources/two-col.html'

    left_column_content = fields.StreamField(
        custom_blocks.AvailableColumnBlocks, 
        default=''
    )

    right_column_content = fields.StreamField(
        custom_blocks.AvailableColumnBlocks, 
        default=''
    )

    body = fields.StreamField(blocks, default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [   
        MultiFieldPanel(
            [
                StreamFieldPanel('left_column_content'),
            ],
            heading="Left column content",
            classname="collapsible"
        ),                 
        MultiFieldPanel(
            [
                StreamFieldPanel('right_column_content'),
            ],
            heading="Right column content",
            classname="collapsible"
        ),            
        MultiFieldPanel(
            [
                StreamFieldPanel('body'),
            ],
            heading="One column content",
            classname="collapsible"
        ),      
    ]

    # Parent page / subpage type rules
    subpage_types = ['ResourcePage']


class ResourcePage(Page):
    template = 'patterns/templates/resources/two-col.html'

    # Database fields
    short_description = models.TextField(max_length=255, null=True, blank=False, default='')

    icon = models.ForeignKey(
        Svg,
        null=True, 
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )    

    left_column_content = fields.StreamField(
        custom_blocks.AvailableColumnBlocks, 
        default=''
    )

    right_column_content = fields.StreamField(
        custom_blocks.AvailableColumnBlocks, 
        default=''
    )

    body = fields.StreamField(blocks, default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        SvgChooserPanel('icon'),
                        FieldPanel('short_description'),
                    ]
                ),
            ],
            heading="Basic info",
            classname="collapsible"
        ),        
        MultiFieldPanel(
            [
                StreamFieldPanel('left_column_content'),
            ],
            heading="Left column content",
            classname="collapsible"
        ),                 
        MultiFieldPanel(
            [
                StreamFieldPanel('right_column_content'),
            ],
            heading="Right column content",
            classname="collapsible"
        ),            
        MultiFieldPanel(
            [
                StreamFieldPanel('body'),
            ],
            heading="Full width content",
            classname="collapsible"
        ),         
    ]    

    # Parent page / subpage type rules
    parent_page_types = ['ResourcesIndexPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['prev_article_title'] = f'Previous Topic: {self.get_prev_sibling().title}' if self.get_prev_sibling() else ''
        context['prev_article_url'] = self.get_prev_sibling().url if self.get_prev_sibling() else ''
        context['next_article_title'] = f'Next Topic: {self.get_next_sibling().title}' if self.get_next_sibling() else ''
        context['next_article_url'] = self.get_next_sibling().url if self.get_next_sibling() else ''
        return context    
