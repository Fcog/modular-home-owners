from functools import reduce
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel, PageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from mhoapp.partners.models import PartnerPage, LocationCategory
from .admin import HomePageForm


class HomesIndexPage(Page):
    # Database fields
    intro = models.CharField(max_length=250, default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    # Parent page / subpage type rules
    subpage_types = ['HomePage']


    def get_template(self, request):
        if request.htmx:
            return 'patterns/molecules/homes-grid/homes-grid.html'
        
        return 'patterns/templates/homes/homes_index_page.html'


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        page = request.GET.get('page')
        styles = request.GET.getlist('style')
        min_price_range = request.GET.get('min-price-range')
        max_price_range = request.GET.get('max-price-range')
        location = request.GET.get('shipping')

        # Get the full unpaginated listing of homes as a queryset.
        homes = HomePage.objects.live()

        # Filter by style.
        if styles and 'all' not in styles:
            homes = homes.filter(reduce(lambda x, y: x | y, [models.Q(style__name__iexact=item) for item in styles]))

        # Filter by price range.            
        if min_price_range:
            homes = homes.filter(cost__gt=int(min_price_range))

        if max_price_range:
            homes = homes.filter(cost__lte=int(max_price_range))        

        # Filter by location.            
        if location and location != 'all':
            homes = homes.filter(partner__locations__code__iexact=location)

        # Set up pagination.
        paginator = Paginator(homes, 6) # Show 6 resources per page        

        try:
            homes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            homes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            homes = paginator.page(paginator.num_pages)                       

        context['activate_inifinite_scroll'] = True

        context['homes'] = homes
       
        context['locations'] = list(map(
            lambda item: {
                'id': item.code,
                'text': item.name,
                'selected': item.code == location,
            },
            LocationCategory.objects.all().order_by('name')
        ))

        context['home_styles'] = list(map(
            lambda item: {
                'id': item.id,
                'label': item.name,
                'value': item.name.lower(),
                'checked': item.name.lower() in styles,
            },
            StyleCategory.objects.all().order_by('name')
        )) 

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
    template = 'patterns/templates/homes/home_page.html'

    # Database fields
    code = models.TextField(max_length=255)
    certified = models.BooleanField(
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
                        FieldPanel('certified'),
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
