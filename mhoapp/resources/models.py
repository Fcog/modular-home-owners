from django.db import models
from wagtail.core import blocks, fields 
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel

from mhoapp.theme import blocks as custom_blocks


class ResourcesIndexPage(Page):
    template = 'patterns/templates/flexible/two-col.html'

    heading = fields.StreamField(
        custom_blocks.TwoColumnsBlockEqualWidth, 
        default=''
    )

    body = fields.StreamField([
        ('Separator', custom_blocks.Separator()),
        ('headingH2', custom_blocks.HeadingH2()),
        ('ResourcesCards', custom_blocks.ResourcesCards()),
        ('ResourcesCTA', custom_blocks.ResourcesCTA()),
        ('PartnersCTA', custom_blocks.PartnersCTA()),
        ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
        ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
        ('articlesCTA', custom_blocks.ArticlesCTABlock()),
        ('ForumCTA', custom_blocks.ForumCTA()),
        ('paragraph', custom_blocks.Paragraph()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        StreamFieldPanel('heading'),
        StreamFieldPanel('body'),
    ]

    # Parent page / subpage type rules
    subpage_types = ['ResourcePage']


class ResourcePage(Page):
    template = 'patterns/templates/flexible/two-col.html'

    # Database fields
    short_description = models.TextField(max_length=255, null=True, blank=False, default='')

    icon = models.ForeignKey(
        Svg,
        null=True, 
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )    

    heading = fields.StreamField(
        custom_blocks.TwoColumnsBlockEqualWidth, 
        default=''
    )

    body = fields.StreamField([
        ('Separator', custom_blocks.Separator()),
        ('headingH2', custom_blocks.HeadingH2()),
        ('ResourcesCTA', custom_blocks.ResourcesCTA()),
        ('PartnersCTA', custom_blocks.PartnersCTA()),
        ('PopularHomesGrid', custom_blocks.PopularHomesGrid()),
        ('GetYourHouseCTA', custom_blocks.GetYourHouseCTA()),
        ('articlesCTA', custom_blocks.ArticlesCTABlock()),
        ('ForumCTA', custom_blocks.ForumCTA()),
        ('paragraph', custom_blocks.Paragraph()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], default='')

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
        StreamFieldPanel('heading'),
        StreamFieldPanel('body'),
    ]    

    # Parent page / subpage type rules
    parent_page_types = ['ResourcesIndexPage']
