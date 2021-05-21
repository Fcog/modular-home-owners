from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks, fields
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailyoast.edit_handlers import YoastPanel

from mhoapp.theme import blocks as custom_blocks


blocks = [
    ('separator', custom_blocks.Separator()),
    ('headingH1', custom_blocks.HeadingH1()),
    ('headingH2', custom_blocks.HeadingH2()),
    ('ResourcesCTA', custom_blocks.ResourcesCTA()),
    ('PartnersCTA', custom_blocks.PartnersCTA()),
    ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
    ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
    ('articlesCTA', custom_blocks.ArticlesCTABlock()),
    ('articlesCTAGlobal', custom_blocks.ArticlesCTAGlobal()),
    ('ForumCTA', custom_blocks.ForumCTA()),
    ('hero', custom_blocks.HeroBlock()),
    ('hero2', custom_blocks.Hero2Block()),
    ('paragraph', custom_blocks.Paragraph()),
    ('threeColumnsBlock', custom_blocks.ThreeColumnsBlock()),
    ('quote', blocks.BlockQuoteBlock()),
    ('image', ImageChooserBlock()),
    ('embed', EmbedBlock()),
]


class FlexibleOneColumnPage(Page):
    template = 'patterns/templates/flexible/one-col.html'

    keywords = models.CharField(default='', blank=True, max_length=100)

    # Database fields
    display_title = models.BooleanField(default=False, blank=True)
    body = StreamField(blocks, default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('display_title'),
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


class FlexibleTwoColumnPage(Page):
    template = 'patterns/templates/flexible/two-col.html'

    keywords = models.CharField(default='', blank=True, max_length=100)

    # Database fields
    offset_2nd_column = models.BooleanField(default=False, blank=True)

    heading = fields.StreamField(
        custom_blocks.TwoColumnsBlockEqualWidth, 
        default=''
    )

    body = StreamField(blocks, default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('offset_2nd_column'),
        StreamFieldPanel('heading'),
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
        return context    