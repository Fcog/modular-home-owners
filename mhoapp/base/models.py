from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, RichTextField
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel


class MHOSettings(models.Model):
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
    contact_email = models.EmailField(max_length=255, default="services@mho.com")
    search_button_text = models.CharField(max_length=254, default="Find Your Home")

    # Filtering default values
    filter_price_min = models.PositiveIntegerField(default="50000", verbose_name="Price range min value")
    filter_price_max = models.PositiveIntegerField(default="1500000", verbose_name="Price range max value")
    filter_price_step = models.PositiveIntegerField(default="10000", verbose_name="Price range widget values step")
    filter_sqft_min = models.PositiveIntegerField(default="50", verbose_name="Square footage min value")
    filter_sqft_max = models.PositiveIntegerField(default="600", verbose_name="Square footage max value")
    filter_sqft_step = models.PositiveIntegerField(default="50", verbose_name="Square footage range widget values step")

    # Forum CTA global data
    forum_title = models.TextField(max_length=255, null=True, verbose_name="Title")
    forum_text = models.TextField(max_length=255, null=True, verbose_name="Text")
    forum_button_text = models.TextField(max_length=255, null=True, verbose_name="Button Text")
    forum_button_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Button url") 
    forum_button_external_url = models.URLField('Button URL', null=True, blank=True)

    # Get Your House CTA global data
    gyh_title = models.TextField(max_length=255, null=True, verbose_name="Title")
    gyh_column_1_title = models.TextField(max_length=255, null=True, verbose_name="Column 1 title")
    gyh_column_1_text = models.TextField(max_length=255, null=True, verbose_name="Column 1 text")
    gyh_column_2_title = models.TextField(max_length=255, null=True, verbose_name="Column 2 title")
    gyh_column_2_text = models.TextField(max_length=255, null=True, verbose_name="Column 2 text")
    gyh_column_3_title = models.TextField(max_length=255, null=True, verbose_name="Column 3 title")
    gyh_column_3_text = models.TextField(max_length=255, null=True, verbose_name="Column 3 text")
    gyh_link_1_text = models.TextField(max_length=255, null=True, verbose_name="Link 1 text")
    gyh_link_1_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Link 1 url") 
    gyh_link_2_text = models.TextField(max_length=255, null=True, verbose_name="Link 2 text")
    gyh_link_2_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Link 2 url") 

    # Partner CTA global data
    partner_1_title = RichTextField(null=True, blank=True)
    partner_1_text = models.TextField(max_length=255, null=True, verbose_name="Column 1 text")     
    partner_1_button_text = models.TextField(max_length=255, null=True, verbose_name="Column 1 button text") 
    partner_1_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Column 1 link url") 
    partner_2_title = RichTextField(null=True, blank=True)
    partner_2_text = models.TextField(max_length=255, null=True, verbose_name="Column 2 text")        
    partner_2_button_text = models.TextField(max_length=255, null=True, verbose_name="Column 2 button text")     
    partner_2_button_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name="Column 2 link url")        

    # Resources CTA global data
    resources_text = RichTextField(null=True, blank=True)

    # Editor panels configuration
    panels = [
        MultiFieldPanel(
            [
                SvgChooserPanel('logo'),
                SvgChooserPanel('logo_white'),
                FieldPanel('contact_email'),
                FieldPanel('search_button_text'),
            ],
            heading="General Setting",
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
        MultiFieldPanel(
            [
                FieldPanel('forum_title'),
                FieldPanel('forum_text'),
                FieldPanel('forum_button_text'),
                PageChooserPanel('forum_button_page'),
                FieldPanel('forum_button_external_url')
            ],
            heading="Forum CTA text",
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
            heading="Get Your House CTA text",
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
            heading="Partners CTA text",
            classname="collapsible collapsed",
        ),        
        MultiFieldPanel(
            [
                FieldPanel('resources_text'),
            ],
            heading="Resources CTA text",
            classname="collapsible collapsed",
        ),            
    ]

    def forum_button_url(self):
        if self.forum_button_page:
            return self.forum_button_page.url
        elif self.forum_button_external_url:
            return self.forum_button_external_url

    def __str__(self):
        return "MHO website settings"
