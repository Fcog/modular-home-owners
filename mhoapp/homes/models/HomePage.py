from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail_multi_upload.edit_handlers import MultipleImagesPanel

from mhoapp.base.models import HomePageSettings
from mhoapp.base.utils import truncate_float, currency
from mhoapp.homes.admin import HomePageForm
from mhoapp.partners.models.PartnerPage import PartnerPage
from mhoapp.homes.models.StyleCategory import StyleCategory


class HomePage(Page):
    template = 'patterns/templates/homes/home-page.html'

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
    link = models.URLField(max_length=300, blank=True)
    floorplans_link = models.URLField(max_length=300, blank=True)
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
                MultipleImagesPanel(
                    'floorplan_gallery_images',
                    label="Floorplan Image Gallery",
                    image_field_name="image"
                ),
                MultipleImagesPanel(
                    'elevation_gallery_images',
                    label="Elevation Image Gallery",
                    image_field_name="image"
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

        global_data = HomePageSettings.for_request(request)

        # Data placeholders formatting.
        # Replaces a Home field with any placeholder with the field name.
        # ex: text: Lorem {home.cost} Ipsum => text: Lorem 500000 Ipsum
        # Docs: https://pyformat.info/#getitem_and_getattr
        # ------------------------------------------------------------------------------
        context['page'].intro = global_data.home_intro.format(home=self) if global_data.home_intro else ''
        
        context['home_form_id'] = global_data.home_form_id

        context['header_theme'] = "blue"

        context['similar_homes'] = HomePage.objects.filter(partner=self.partner).exclude(id=self.id).live()[:3]

        return context

    @property
    def bedrooms_text(self):    
        return 'Bedroom' if self.bedrooms == 1 else 'Bedrooms' 

    @property
    def baths_text(self):
        return 'Bath' if self.baths == 1.0 else 'Baths'

    @property
    def stories_text(self):
        return 'Story' if self.stories == 1.0 else 'Stories' 

    @property
    def stories_formatted(self):
        return truncate_float(self.stories)        

    @property
    def baths_formatted(self):
        return truncate_float(self.baths)

    @property
    def cost_formatted(self):
        return currency(self.cost)      

    @property
    def estimated_cost_formatted(self):
        return currency(self.estimated_cost)        