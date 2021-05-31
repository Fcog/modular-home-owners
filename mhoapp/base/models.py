from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, RichTextField
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class GeneralSettings(BaseSetting):
    # Database fields
    # General Settings
    logo = models.ForeignKey(
        Svg,
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    logo_white = models.ForeignKey(
        Svg,
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contact_email = models.EmailField(max_length=255, null=True, default="services@mho.com")
    search_button_text = models.CharField(max_length=254, null=True,  default="Find Your Home")

    # Editor panels configuration
    panels = [
        SvgChooserPanel('logo'),
        SvgChooserPanel('logo_white'),
        FieldPanel('contact_email'),
        FieldPanel('search_button_text'),
    ]


@register_setting
class HomePageSettings(BaseSetting):
    home_intro = models.TextField(max_length=255, null=True, verbose_name="Home introduction", default="")
    home_button_text = models.CharField(max_length=255, null=True, verbose_name="Button text", default="")
    home_small_text = models.TextField(max_length=255, null=True, verbose_name="Small text", default="")
    home_verified_title = models.CharField(max_length=255, null=True, verbose_name="Verified box title", default="")
    home_verified_text = models.CharField(max_length=255, null=True, verbose_name="Verified box text", default="")
    home_tooltip_text = models.TextField(max_length=255, null=True, verbose_name="Est Cost tooltip text", default="")
    home_similar_title = models.CharField(max_length=255, null=True, verbose_name="Similar houses section title", default="")
    home_similar_button_text = models.CharField(max_length=254, null=True, verbose_name="Similar houses button text",  default="Search All Homes")
    home_similar_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Similar houses button link")    
    home_form_id = models.CharField(max_length=20, null=True, verbose_name="Wufoo Form ID", default="")
    home_form_height = models.IntegerField(null=True, verbose_name="Wufoo Form Height in pixels", default="500")

    # Editor panels configuration
    panels = [
        FieldPanel('home_intro'),
        FieldPanel('home_button_text'),
        FieldPanel('home_small_text'),
        FieldPanel('home_verified_title'),
        FieldPanel('home_verified_text'),
        FieldPanel('home_tooltip_text'),
        FieldPanel('home_similar_title'),
        FieldPanel('home_similar_button_text'),
        PageChooserPanel('home_similar_button_link'),
        FieldPanel('home_form_id'),
        FieldPanel('home_form_height'),
    ]    


@register_setting
class HomeSearchPageSettings(BaseSetting):
    homes_search_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Homes Search Page")    
    homes_ad_text = models.CharField(max_length=254, null=True, default="")
    homes_ad_button_text = models.CharField(max_length=255, null=True, verbose_name="Button text", default="")     
    homes_ad_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Button URL from a page")    
    homes_ad_external_url = models.URLField('Button external URL', null=True, blank=True, default="")        

    filter_price_min = models.PositiveIntegerField(default="50000", null=True, verbose_name="Price range min value")
    filter_price_max = models.PositiveIntegerField(default="1500000", null=True, verbose_name="Price range max value")
    filter_price_step = models.PositiveIntegerField(default="10000", null=True, verbose_name="Price range widget values step")
    filter_sqft_min = models.PositiveIntegerField(default="50", null=True, verbose_name="Square footage min value")
    filter_sqft_max = models.PositiveIntegerField(default="600", null=True, verbose_name="Square footage max value")
    filter_sqft_step = models.PositiveIntegerField(default="50", null=True, verbose_name="Square footage range widget values step")    

    def homes_ad_button_url(self):
        if self.homes_ad_button_link:
            return self.homes_ad_button_link.url
        elif self.homes_ad_external_url:
            return self.homes_ad_external_url        

    panels = [
        MultiFieldPanel(
            [
                PageChooserPanel('homes_search_page'),
            ],
            heading="General Settings",
            classname="collapsible collapsed",
        ),        
        MultiFieldPanel(
            [
                FieldPanel('homes_ad_text'),
                FieldPanel('homes_ad_button_text'),
                PageChooserPanel('homes_ad_button_link'),
                FieldPanel('homes_ad_external_url'),  
            ],
            heading="Homes search ad",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('filter_price_min'),
                FieldPanel('filter_price_max'),
                FieldPanel('filter_price_step'),
                FieldPanel('filter_sqft_min'),
                FieldPanel('filter_sqft_max'),
                FieldPanel('filter_sqft_step'),
            ],
            heading="Filtering Default Values",
            classname="collapsible collapsed",
        ),        
    ]    


@register_setting
class BlocksSettings(BaseSetting):   
    # Forum CTA global data
    forum_title = models.TextField(max_length=255, null=True, verbose_name="Title", default="")
    forum_text = models.TextField(max_length=255, null=True, verbose_name="Text", default="")
    forum_button_text = models.TextField(max_length=255, null=True, verbose_name="Button Text", default="")
    forum_button_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Button URL from a page") 
    forum_button_external_url = models.URLField('Button external URL', null=True, blank=True, default="")

    # Get Your House CTA global data
    gyh_title = models.TextField(max_length=255, null=True, verbose_name="Title", default="")
    gyh_column_1_title = models.TextField(max_length=255, null=True, verbose_name="Column 1 title", default="")
    gyh_column_1_text = models.TextField(max_length=255, null=True, verbose_name="Column 1 text", default="")
    gyh_column_2_title = models.TextField(max_length=255, null=True, verbose_name="Column 2 title", default="")
    gyh_column_2_text = models.TextField(max_length=255, null=True, verbose_name="Column 2 text", default="")
    gyh_column_3_title = models.TextField(max_length=255, null=True, verbose_name="Column 3 title", default="")
    gyh_column_3_text = models.TextField(max_length=255, null=True, verbose_name="Column 3 text", default="")
    gyh_link_1_text = models.TextField(max_length=255, null=True, verbose_name="Link 1 text", default="")
    gyh_link_1_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Link 1 URL") 
    gyh_link_2_text = models.TextField(max_length=255, null=True, verbose_name="Link 2 text", default="")
    gyh_link_2_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Link 2 URL") 

    # Partner CTA global data
    partner_1_title = RichTextField(null=True, blank=True, default="", features=['bold'])
    partner_1_text = models.TextField(max_length=255, null=True, verbose_name="Column 1 text", default="")     
    partner_1_button_text = models.TextField(max_length=255, null=True, verbose_name="Column 1 button text", default="") 
    partner_1_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Column 1 link URL") 
    partner_2_title = RichTextField(null=True, blank=True, default="")
    partner_2_text = models.TextField(max_length=255, null=True, verbose_name="Column 2 text", default="")        
    partner_2_button_text = models.TextField(max_length=255, null=True, verbose_name="Column 2 button text", default="")     
    partner_2_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Column 2 link URL")  

    # Articles CTA global data
    art_cta_col_intro = RichTextField(null=True, blank=True, default="", features=['bold'])

    art_cta_col_1_title = models.TextField(max_length=255, null=True, blank=True, default="", verbose_name="Column 1 Title")
    art_cta_col_1_link_1 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=False, null=True, related_name='+', verbose_name="Column 1 Link 1")
    art_cta_col_1_link_2 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Column 1 Link 2")
    art_cta_col_1_link_3 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Column 1 Link 3")
    art_cta_col_1_link_4 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Column 1 Link 4")

    art_cta_col_2_title = models.TextField(max_length=255, null=True, blank=True, default="", verbose_name="Column 2 Title")
    art_cta_col_2_link_1 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=False, null=True, related_name='+', verbose_name="Column 2 Link 1")
    art_cta_col_2_link_2 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Column 2 Link 2")
    art_cta_col_2_link_3 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Column 2 Link 3")
    art_cta_col_2_link_4 = models.ForeignKey('articles.ArticlePage', on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Column 2 Link 4")    

    art_cta_button_text = models.TextField(max_length=255, null=True, blank=True, default="", verbose_name="Button text")     
    art_cta_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Button Link")  

    # Resources CTA global data
    resources_text = RichTextField(null=True, blank=True, default="")    

    def forum_button_url(self):
        if self.forum_button_page:
            return self.forum_button_page.url
        elif self.forum_button_external_url:
            return self.forum_button_external_url    

    # Editor panels configuration
    panels = [
        MultiFieldPanel(
            [
                FieldPanel('forum_title'),
                FieldPanel('forum_text'),
                FieldPanel('forum_button_text'),
                PageChooserPanel('forum_button_page'),
                FieldPanel('forum_button_external_url')
            ],
            heading="Forum CTA",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('gyh_title'),
                FieldPanel('gyh_column_1_title'),
                FieldPanel('gyh_column_1_text'),
                FieldPanel('gyh_column_2_title'),
                FieldPanel('gyh_column_2_text'),
                FieldPanel('gyh_column_3_title'),
                FieldPanel('gyh_column_3_text'),
                FieldPanel('gyh_link_1_text'),
                PageChooserPanel('gyh_link_1_link'),
                FieldPanel('gyh_link_2_text'),
                PageChooserPanel('gyh_link_2_link'),
            ],
            heading="Get Your House CTA",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('partner_1_title'),
                FieldPanel('partner_1_text'),
                FieldPanel('partner_1_button_text'),
                PageChooserPanel('partner_1_button_link'),
                FieldPanel('partner_2_title'),
                FieldPanel('partner_2_text'),
                FieldPanel('partner_2_button_text'),
                PageChooserPanel('partner_2_button_link'),
            ],
            heading="Partners CTA",
            classname="collapsible collapsed",
        ),        
        MultiFieldPanel(
            [
                FieldPanel('resources_text'),
            ],
            heading="Resources CTA",
            classname="collapsible collapsed",
        ),       
        MultiFieldPanel(
            [
                FieldPanel('art_cta_col_intro'),
                FieldPanel('art_cta_col_1_title'),
                PageChooserPanel('art_cta_col_1_link_1'),
                PageChooserPanel('art_cta_col_1_link_2'),
                PageChooserPanel('art_cta_col_1_link_3'),
                PageChooserPanel('art_cta_col_1_link_4'),
                FieldPanel('art_cta_col_2_title'),
                PageChooserPanel('art_cta_col_2_link_1'),
                PageChooserPanel('art_cta_col_2_link_2'),
                PageChooserPanel('art_cta_col_2_link_3'),
                PageChooserPanel('art_cta_col_2_link_4'),
                FieldPanel('art_cta_button_text'),
                PageChooserPanel('art_cta_button_link'),                
            ],
            heading="Articles CTA",
            classname="collapsible collapsed",
        ),               
    ]    