from django.apps import apps
from wagtail.core import blocks


class PartnerTypeGrid(blocks.ChoiceBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        PartnerType = apps.get_model('partners', 'PartnerTypePage').objects.get(pk=value)

        context['list'] = list(map(
            lambda item: {
                'image': item.logo,
                'url': item.url,
            },
            apps.get_model('partners', 'PartnerPage').objects.live().descendant_of(PartnerType)
        ))

        return context

    class Meta:
        label = 'Partners per type Grid'
        icon = 'placeholder'
        template = 'patterns/organisms/icons-list/icons-list.html'