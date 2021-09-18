import re
from functools import reduce
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.core.models import Page
from wagtail.core import blocks, fields
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from mhoapp.base.utils import truncate_float, currency
from mhoapp.base.models import HomeSearchPageSettings
from mhoapp.homes.models.HomePage import HomePage
from mhoapp.homes.models.StyleCategory import StyleCategory
from mhoapp.partners.models.LocationCategory import LocationCategory
from mhoapp.theme import blocks as custom_blocks


class HomesIndexPage(Page):
    LEFT_SHORTER = 'LS'
    EQUAL_WIDTH = 'EW'
    FULL_WIDTH = 'FW'

    COLUMNS_LAYOUT = [
        (FULL_WIDTH, '1 Column - Full width'),
        (LEFT_SHORTER, '2 Columns - Left side smaller'),
        (EQUAL_WIDTH, '2 Columns - Equal width'),
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

    initial_home_style = models.ForeignKey(
        'homes.StyleCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Initial Home Style"
    )    

    layout = models.CharField(
        max_length=2,
        choices=COLUMNS_LAYOUT,
        default=FULL_WIDTH,
        verbose_name="Top content layout"
    )

    left_col_content = fields.StreamField(
        custom_blocks.AvailableColumnBlocks, 
        default='', 
        blank=True, 
    )    

    right_col_content = fields.StreamField(
        custom_blocks.AvailableColumnBlocks, 
        default='', 
        blank=True, 
    )        

    full_content = fields.StreamField(
        [
            ('headingH1', custom_blocks.HeadingH1()),
            ('headingH2', custom_blocks.HeadingH2()),
            ('partnersButtons', custom_blocks.PartnersButtons()),
            ('readMoreText', custom_blocks.ReadMoreText()),
            ('blueBoxCTA', custom_blocks.BlueBoxCTA()),
            ('paragraph', custom_blocks.Paragraph()),
            ('image', ImageChooserBlock()),
            ('embed', EmbedBlock()),
        ], 
        default='', 
        blank=True, 
    )

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        SnippetChooserPanel('initial_price_range'),
                        SnippetChooserPanel('initial_location'),
                        SnippetChooserPanel('initial_home_style'),
                    ]
                )
            ],
            heading="Homes Search Filtering Initial Values",
            classname="collapsible collapsed"
        ),        
        FieldPanel('layout'),
        StreamFieldPanel('left_col_content', classname="js-left-col-panel"),
        StreamFieldPanel('right_col_content', classname="js-right-col-panel"),
        StreamFieldPanel('full_content', classname="js-full-content-panel"),
    ]

    # Parent page / subpage type rules
    subpage_types = ['HomePage']

    def get_template(self, request):
        if request.htmx:
            return 'patterns/molecules/homes-grid/homes-grid-content.html'
        
        return 'patterns/templates/homes/homes-index-page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        global_data = HomeSearchPageSettings.for_request(request)

        # Price Range initial values.
        # ------------------------------------------------------------------------------------- 
        initial_min_price_range = self.initial_price_range.get_min_price_range() if self.initial_price_range else global_data.filter_price_min
        initial_max_price_range = self.initial_price_range.get_max_price_range() if self.initial_price_range else global_data.filter_price_max

        # Filtering logic.
        # -------------------------------------------------------------------------------------
        page = request.GET.get('page')
        styles = [self.initial_home_style.name.lower()] if self.initial_home_style else request.GET.getlist('style')

        # The prices values are formatted as money, so we use a regex substitution to convert it to an integer. 
        min_price_range = re.sub('\D', '', request.GET.get('min-price-range')) if request.GET.get('min-price-range') else initial_min_price_range
        max_price_range = re.sub('\D', '', request.GET.get('max-price-range')) if request.GET.get('max-price-range') else initial_max_price_range

        location = self.initial_location.code if self.initial_location else request.GET.get('shipping')
        min_sqft = request.GET.get('min-sqft')
        max_sqft = request.GET.get('max-sqft')
        bedrooms = request.GET.get('bedrooms')
        bathrooms = request.GET.get('bathrooms')
        partner = request.GET.get('partner')

        # Get the full unpaginated listing of homes as a queryset.
        homes = HomePage.objects.live().order_by('cost')

        # Filter by partner
        if partner:
            homes = homes.filter(partner__slug=partner)

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
        paginator = Paginator(homes, 8)    

        try:
            homes = paginator.page(page)

            # Tweak to insert the 6th card from the page 1 (page 1 has a pagination of 5) into the page 2.
            #if page == '2':
                #homes = paginator.object_list[5:13]            
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            homes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            homes = paginator.page(paginator.num_pages)               

        # Set up the Home Ad
        # -------------------------------------------------------------------------------------
        # Used to show the ad in the 1st page.
        context['show_add'] = True if not page else False               
        context['home_cta_form_id'] = global_data.homes_ad_form_id
        context['home_cta_form_height'] = global_data.homes_ad_form_height

        # Add the homes data to the page context.
        # -------------------------------------------------------------------------------------        
        context['homes'] = homes  

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

        context['min_price_range'] = min_price_range
        context['max_price_range'] = max_price_range

        return context     
