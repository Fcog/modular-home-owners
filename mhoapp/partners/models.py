from django.db import models
from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from .admin import PartnerTypePageForm


class PartnersIndexPage(Page):
    template = 'patterns/pages/archive/archive.html'

    # Parent page / subpage type rules
    subpage_types = ['PartnerTypePage']


class PartnerTypePage(Page):
    template = 'patterns/templates/partners/partner_type_page.html'

    # Database fields
    intro = models.CharField(max_length=250, default='')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['PartnersIndexPage']
    subpage_types = ['PartnerPage']

    # Admin custom changes
    base_form_class = PartnerTypePageForm


@register_snippet
class LocationCategory(models.Model):
    # Database fields
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, default="")

    # Editor panels configuration
    panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('name'),
                        FieldPanel('code'),
                    ]
                )
            ]
        )
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'locations of partners'


class PartnerPage(Page):
    template = 'patterns/templates/partners/partner_page.html'

    # Database fields
    name = models.TextField(max_length=255)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    phone = models.TextField(max_length=25)
    website = models.URLField()
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    locations = ParentalManyToManyField(LocationCategory)

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('name'),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel('phone'),
                        FieldPanel('website'),
                    ]
                ),
            ],
            heading="Basic info",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('locations', widget=forms.CheckboxSelectMultiple),
            ],
            heading="Locations",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel('logo'),
                ImageChooserPanel('main_image'),
                InlinePanel(
                    'gallery_images',
                    label="Image Gallery"
                ),
            ],
            heading="Images",
            classname="collapsible collapsed"
        ),
    ]

    def PartnerType(self):
        return self.get_parent()

    # Parent page / subpage type rules
    parent_page_types = ['PartnerTypePage']


class PartnerGalleryImage(Orderable):
    # Database fields
    page = ParentalKey(
        PartnerPage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    # Editor panels configuration
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
