from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from mhoapp.base.models import MHOSettings
from mhoapp.base.utils import truncate_float, currency
from mhoapp.homes.admin import HomePageForm
from mhoapp.partners.models import PartnerPage
from mhoapp.homes.models.StyleCategory import StyleCategory


class HomePage(Page):
    template = 'patterns/templates/homes/home_page.html'

    # Database fields
    code = models.TextField(max_length=255)
    verified = models.BooleanField(
        null=False,
        default=False,
    )
    sqft = models.PositiveSmallIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    baths = models.FloatField()
    stories = models.FloatField()
    cost = models.PositiveIntegerField()
    estimated_cost = models.PositiveIntegerField()
    link = models.URLField(blank=True)
    floorplans_link = models.URLField(blank=True)
    info = models.TextField(blank=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    style = models.ForeignKey(
        StyleCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    partner = models.ForeignKey(
        PartnerPage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    # Custom search fields
    search_fields = Page.search_fields + [
        index.FilterField('style'),
        index.SearchField('cost'),
        index.FilterField('bedrooms'),
        index.RelatedFields('partner', [
            index.FilterField('locations'),
        ]),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('code'),
                        FieldPanel('verified'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('sqft'),
                        FieldPanel('bedrooms'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('baths'),
                        FieldPanel('stories'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('cost'),
                        FieldPanel('estimated_cost'),
                    ]
                ),
                SnippetChooserPanel('style'),
                PageChooserPanel('partner', 'partners.PartnerPage'),
                FieldPanel('link'),
                FieldPanel('floorplans_link'),
                FieldPanel('info'),
                ImageChooserPanel('main_image'),
                InlinePanel(
                    'floorplan_gallery_images',
                    label="Floorplan Image Gallery"
                ),
                InlinePanel(
                    'elevation_gallery_images',
                    label="Elevation Image Gallery"
                ),
            ],
            heading="Basic info",
            classname="collapsible"
        ),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['HomesIndexPage']

    # Admin custom changes
    base_form_class = HomePageForm

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        global_data = MHOSettings.objects.first()

        # Home data formatting.
        # ------------------------------------------------------------------------------
        self.cost = currency(self.cost)
        self.estimated_cost = currency(self.estimated_cost)

        context['page'].baths = truncate_float(self.baths)
        context['page'].stories = truncate_float(self.stories)
        context['page'].bedrooms_text = 'Bedroom' if self.bedrooms == 1 else 'Bedrooms' 
        context['page'].baths_text = 'Bath' if self.baths == 1.0 else 'Baths' 
        context['page'].stories_text = 'Story' if self.stories == 1.0 else 'Stories' 

        context['page'].intro = global_data.home_intro.format(home=self) if global_data.home_intro else ''
        
        # Header theme
        # ------------------------------------------------------------------------------
        context['header_theme'] = "blue"

        return context