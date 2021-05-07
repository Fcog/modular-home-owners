from functools import reduce
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from mhoapp.base.models import MHOSettings
from mhoapp.homes.models.HomePage import HomePage
from mhoapp.homes.models.StyleCategory import StyleCategory
from mhoapp.partners.models import LocationCategory
from mhoapp.theme.models import BlueBoxCTA, ReadMoreText, PartnersButtons, Paragraph


class HomesIndexPage(Page):
    LEFT_SHORTER = 'LS'
    EQUAL_WIDTH = 'EW'
    FULL_WIDTH = 'FW'

    COLUMNS_LAYOUT = [
        (FULL_WIDTH, '1 Column - Full width'),
        (LEFT_SHORTER, '2 Columns - Left side smaller'),
        (EQUAL_WIDTH, '2 Columns - Equal width'),
    ]

    blocks = [
        ('partnersButtons', PartnersButtons()),
        ('readMoreText', ReadMoreText()),
        ('blueBoxCTA', BlueBoxCTA()),
        ('paragraph', Paragraph()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ]

    # Database fields
    initial_price_range = models.ForeignKey(
        'homes.PriceRanges',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Initial Price Range"
    )

    initial_location = models.ForeignKey(
        'partners.LocationCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Initial location"
    )    

    layout = models.CharField(
        max_length=2,
        choices=COLUMNS_LAYOUT,
        default=FULL_WIDTH,
        verbose_name="Heading layout"
    )

    left_content = StreamField(blocks, default='', verbose_name='Heading Left Content')
    right_content = StreamField(blocks, default='', blank=True, verbose_name='Heading Right Content')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        SnippetChooserPanel('initial_price_range'),
                        SnippetChooserPanel('initial_location'),
                    ]
                )
            ],
            heading="Homes Search Filtering Initial Values",
            classname="collapsible"
        ),        
        FieldPanel('layout'),
        StreamFieldPanel('left_content'),
        StreamFieldPanel('right_content'),
    ]

    # Parent page / subpage type rules
    subpage_types = ['HomePage']

    def get_template(self, request):
        if request.htmx:
            return 'patterns/molecules/homes-grid/homes-grid.html'
        
        return 'patterns/templates/homes/homes_index_page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        global_data = MHOSettings.objects.first()

        # Price Range initial values.
        # ------------------------------------------------------------------------------------- 
        initial_min_price_range = self.initial_price_range.get_min_price_range() if self.initial_price_range else None
        initial_max_price_range = self.initial_price_range.get_max_price_range() if self.initial_price_range else None
        context['initial_min_price_range'] = initial_min_price_range
        context['initial_max_price_range'] = initial_max_price_range

        # Filtering logic.
        # -------------------------------------------------------------------------------------
        page = request.GET.get('page')
        styles = request.GET.getlist('style')
        min_price_range = initial_min_price_range if initial_min_price_range else request.GET.get('min-price-range') 
        max_price_range = initial_max_price_range if initial_max_price_range else request.GET.get('max-price-range') 
        location = self.initial_location.code if self.initial_location else request.GET.get('shipping')
        min_sqft = request.GET.get('min-sqft')
        max_sqft = request.GET.get('max-sqft')
        bedrooms = request.GET.get('bedrooms')
        bathrooms = request.GET.get('bathrooms')

        # Get the full unpaginated listing of homes as a queryset.
        homes = HomePage.objects.live().order_by('title')

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

        # Filter by square footage.
        if min_sqft:
            homes = homes.filter(sqft__gt=int(min_sqft))

        # Filter by square footage.
        if min_sqft:
            homes = homes.filter(sqft__gt=int(min_sqft))            

        if max_sqft:
            homes = homes.filter(sqft__lte=int(max_sqft))            

        # Filter by bedrooms.
        if bedrooms and bedrooms != '0':
            homes = homes.filter(bedrooms=int(bedrooms))            

        # Filter by bathrooms.
        if bathrooms and bathrooms != '0':
            homes = homes.filter(baths=int(bathrooms))                

        # Total homes found before doing pagination.    
        # -------------------------------------------------------------------------------------
        context['total_homes'] = len(homes)              

        # Set up pagination.
        # -------------------------------------------------------------------------------------
        # Render 5 cards on the 1st page to insert the homes ad.
        pagination = 5 if not page else 6

        paginator = Paginator(homes, pagination, 3)    

        try:
            homes = paginator.page(page)

            # Tweak to insert the 6th card from the page 1 (page 1 has a pagination of 5) into the page 2.
            if page == '2':
                homes = paginator.object_list[5:13]            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            homes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            homes = paginator.page(paginator.num_pages)               

        # Used to show the ad in the 1st page.
        context['pagination'] = pagination               

        # Add the homes data to the page context.
        # -------------------------------------------------------------------------------------
        context['homes'] = homes    

        context['homes_ad_button_url'] = global_data.homes_ad_button_url()

        # Tweak for infinite scroll.
        # -------------------------------------------------------------------------------------
        context['activate_inifinite_scroll'] = True
       
       # Filters initial values.
       # -------------------------------------------------------------------------------------
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

        context['bedrooms_initial_value'] = bedrooms or 0
        context['bathrooms_initial_value'] = bathrooms or 0

        return context     