from django.db import models
from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel

from .admin import PartnerTypePageForm


class PartnersIndexPage(Page):
    template = 'patterns/pages/archive/archive.html'

    # Parent page / subpage type rules
    subpage_types = ['PartnerTypePage']


class PartnerTypePage(Page):
    # Database fields
    icon = models.ForeignKey(
        Svg,
        null=True, 
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Editor panels configuration
    content_panels = Page.content_panels + [
        SvgChooserPanel('icon'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['PartnersIndexPage']
    subpage_types = ['PartnerPage']

    # Admin custom changes
    base_form_class = PartnerTypePageForm

    def get_template(self, request):
        if request.htmx:
            return 'patterns/molecules/icons-list/icons-list.html'
        # 'patterns/templates/partners/partner_type_page.html'
        return 'patterns/molecules/icons-list/icons-list.html'  

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        partners = PartnerPage.objects.child_of(self).live()

        location = request.GET.get('location')

        if location:
            partners = partners.filter(locations__code=location)

        context['list'] = list(map(
            lambda item: {
                'title': item.title,
                'url': item.url,
                'image': item.logo,
            },
            partners.specific()
         ))     

        return context        


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
