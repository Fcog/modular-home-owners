from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from mhoapp.partners.models import PartnerPage
from .admin import HomePageForm


class HomesIndexPage(Page):
    template = 'patterns/pages/homes/homes_index_page.html'

    # Database fields
    intro = models.CharField(max_length=250, default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    # Parent page / subpage type rules
    subpage_types = ['HomePage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        style = request.GET.get('style')
        price_range = request.GET.get('price-range')

        filtered_objects = HomePage.objects

        if style is None and price_range is None or style == 'all' and price_range == 'all':
            filtered_objects = filtered_objects.all()
        else:
            if style and style != 'all':
                filtered_objects = filtered_objects.filter(style__name__iexact=style)
            if price_range and price_range != 'all':
                filtered_objects = price_range_filter(filtered_objects, price_range)

        context['data'] = filtered_objects

        return context


@register_snippet
class StyleCategory(models.Model):
    # Database fields
    name = models.CharField(max_length=255)

    # Editor panels configuration
    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'styles of homes'


@register_snippet
class PriceRanges(models.Model):
    UNDER = 'UN'
    OVER = 'OV'

    # Database fields
    type = models.CharField(
        max_length=2,
        choices=[
            (UNDER, 'Under'),
            (OVER, 'Over'),
        ],
        default=UNDER,
    )
    price = models.PositiveIntegerField(default=0)

    # Editor panels configuration
    panels = [
        FieldPanel('type'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return self.get_type_display() + ' ' + str(self.price)

    class Meta:
        verbose_name_plural = 'price ranges'


class HomePage(Page):
    template = 'patterns/pages/homes/home_page.html'

    # Database fields
    code = models.TextField(max_length=255)
    rating = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
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
                        FieldPanel('rating'),
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
            classname="collapsible collapsed"
        ),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['HomesIndexPage']

    # Admin custom changes
    base_form_class = HomePageForm


class FloorplanGalleryImage(Orderable):
    # Database fields
    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='floorplan_gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        null=True,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    # Editor panels configuration
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ElevationGalleryImage(Orderable):
    # Database fields
    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='elevation_gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        null=True,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    # Editor panels configuration
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


def price_range_filter(filtered_objects, value):
    switcher = {
        'under-50000': filtered_objects.filter(cost__gte=0, cost__lte=50000),
        'under-100000': filtered_objects.filter(cost__gt=50000, cost__lte=100000),
        'under-200000': filtered_objects.filter(cost__gt=100000, cost__lte=200000),
        'under-300000': filtered_objects.filter(cost__gt=200000, cost__lte=300000),
        'over-300000': filtered_objects.filter(cost__gt=300000),
    }
    return switcher.get(value, filtered_objects)