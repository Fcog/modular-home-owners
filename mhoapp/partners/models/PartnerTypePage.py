from django.apps import apps
from django.db import models
from wagtail.core import blocks, fields 
from wagtail.core.models import Page
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from mhoapp.partners.admin import PartnerTypePageForm
from mhoapp.theme import blocks as custom_blocks


def get_partner_types():
    return tuple(PartnerTypePage.objects.values_list('id','title'))


class PartnerTypePage(Page):
    # Database fields
    icon = models.ForeignKey(
        Svg,
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    icon_inverted = models.ForeignKey(
        Svg,
        null=True, 
        blank=True,
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

    body = fields.StreamField([
        ('Separator', custom_blocks.Separator()),
        ('headingH2', custom_blocks.HeadingH2()),
        ('PartnerTypeGrid', custom_blocks.PartnerTypeGrid(choices=get_partner_types)),
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
                        SvgChooserPanel('icon_inverted'),
                    ]
                ),
            ],
            heading="Icons",
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
    parent_page_types = ['PartnersIndexPage']
    subpage_types = ['PartnerPage']

    # Admin custom changes
    base_form_class = PartnerTypePageForm

    def get_template(self, request):
        if request.htmx:
            return 'patterns/molecules/icons-list/icons-list.html'

        return 'patterns/templates/flexible/two-col.html' 

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        partners = apps.get_model('partners', 'PartnerPage').objects.child_of(self).live()

        location = request.GET.get('location')

        if location:
            partners = partners.filter(locations__code=location)

        context['list'] = list(map(
            lambda item: {
                'title': item.title,
                'url': item.url,
                'image': item.logo,
            },
            partners.specific()
         ))     

        if request.htmx:
            context['small_size'] = True

        return context        
