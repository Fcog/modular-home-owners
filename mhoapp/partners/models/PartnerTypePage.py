from django.db import models
from wagtail.core.models import Page
from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel

from mhoapp.partners.admin import PartnerTypePageForm
from .PartnerPage import PartnerPage


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

        return 'patterns/templates/flexible/one-col.html' 

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
