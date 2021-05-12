from django.db import models
from wagtail.core import blocks
from wagtail.core import fields
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from mhoapp.partners.admin import PartnerTypePageForm
from .PartnerPage import PartnerPage
from mhoapp.theme.blocks import *


class PartnerTypePage(Page):
    # Database fields
    icon = models.ForeignKey(
        Svg,
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    heading = fields.StreamField(
        TwoColumnsBlock, 
        default=''
    )

    body = StreamField([
        ('headingH1', HeadingH1()),
        ('headingH2', HeadingH2()),
        ('ResourcesCTA', ResourcesCTA()),
        ('PartnersCTA', PartnersCTA()),
        ('PopularHomesGrid', PopularHomesGrid()),
        ('GetYourHouseCTA', GetYourHouseCTA()),
        ('articlesCTA', ArticlesCTABlock()),
        ('ForumCTA', ForumCTA()),
        ('hero', HeroBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('text', blocks.TextBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        SvgChooserPanel('icon'),
        StreamFieldPanel('heading'),
        StreamFieldPanel('body'),
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

        partners = PartnerPage.objects.child_of(self).live()

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

        return context        
