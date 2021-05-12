from wagtail.core import blocks

from mhoapp.partners.models.LocationCategory import LocationCategory
from mhoapp.partners.models.PartnerTypePage import PartnerTypePage


class PartnersButtons(blocks.ChoiceBlock):
    choices = tuple(LocationCategory.objects.values_list('code','name'))

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        context['buttons'] = list(map(
            lambda item: {
                'hx_get': f'{item.url}?location={value}',
                'hx_target': '#ajax-response',
                'text': f'{value} {item.title}',
                'image': item.icon.url,
            },
            PartnerTypePage.objects.all()
        ))

        return context

    class Meta:
        label = 'Partners by State Buttons'
        icon = 'placeholder'
        template = 'patterns/organisms/partners-buttons/partners-buttons.html'