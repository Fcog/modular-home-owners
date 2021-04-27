from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
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

    # Forum CTA global data
    forum_title = models.TextField(max_length=255, null=True)
    forum_text = models.TextField(max_length=255, null=True)
    forum_button_text = models.TextField(max_length=255, null=True)
    forum_button_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+') 
    forum_button_external_url = models.URLField('Button URL', null=True, blank=True)

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
        ),
    ]

    def forum_button_url(self):
        if self.forum_button_page:
            return self.forum_button_page.url
        elif self.forum_button_external_url:
            return self.forum_button_external_url

    def __str__(self):
        return "MHO website settings"
