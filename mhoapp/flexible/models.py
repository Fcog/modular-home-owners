from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks, fields
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, TabbedInterface, ObjectList
from wagtail.embeds.blocks import EmbedBlock
from wagtailyoast.edit_handlers import YoastPanel

from mhoapp.theme import blocks as custom_blocks


blocks = [
    ('separator', custom_blocks.Separator()),
    ('headingH1Paragraph', custom_blocks.HeadingH1Paragraph()),
    ('ResourcesCTA', custom_blocks.ResourcesCTA()),
    ('PartnersCTA', custom_blocks.PartnersCTA()),
    ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
    ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
    ('articlesCTA', custom_blocks.ArticlesCTABlock()),
    ('articlesCTAGlobal', custom_blocks.ArticlesCTAGlobal()),
    ('ForumCTA', custom_blocks.ForumCTA()),
    ('homesMap', custom_blocks.HomesMap()),
    ('hero', custom_blocks.HeroBlock()),
    ('hero2', custom_blocks.Hero2Block()),
    ('paragraphSection', custom_blocks.ParagraphSection()),
    ('threeColumnsBlock', custom_blocks.ThreeColumnsBlock()),
    ('form', custom_blocks.FormBlock()),
    ('quote', custom_blocks.GreenQuote()),
    ('quote2', custom_blocks.BlueQuote()),
    ('image', custom_blocks.ImageCaption()),
    ('embed', EmbedBlock()),
]


class FlexibleOneColumnPage(Page):
    template = 'patterns/templates/flexible/one-col.html'

    keywords = models.CharField(default='', blank=True, max_length=100)

    # Database fields
    body = StreamField(blocks, default='')

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
        context['header_show_title'] = False
        return context    


class FlexibleOneColumnPageBlueHeader(Page):
    template = 'patterns/templates/articles/single.html'

    keywords = models.CharField(default='', blank=True, max_length=100)

    # Database fields
    body = StreamField([
    ('separator', custom_blocks.Separator()),
    ('ResourcesCTA', custom_blocks.ResourcesCTA()),
    ('PartnersCTA', custom_blocks.PartnersCTA()),
    ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
    ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
    ('articlesCTA', custom_blocks.ArticlesCTABlock()),
    ('articlesCTAGlobal', custom_blocks.ArticlesCTAGlobal()),
    ('ForumCTA', custom_blocks.ForumCTA()),
    ('homesMap', custom_blocks.HomesMap()),
    ('paragraphSection', custom_blocks.ParagraphSection()),
    ('threeColumnsBlock', custom_blocks.ThreeColumnsBlock()),
    ('form', custom_blocks.FormBlock()),
    ('quote', custom_blocks.GreenQuote()),
    ('quote2', custom_blocks.BlueQuote()),
    ('image', custom_blocks.ImageCaption()),
    ('embed', EmbedBlock()),
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
        verbose_name = "Flexible one column page (Blue header)"        