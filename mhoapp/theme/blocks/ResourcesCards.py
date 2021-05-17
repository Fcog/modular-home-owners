from django.apps import apps
from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class ResourcesCards(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])
          
        context['cards'] = apps.get_model('resources', 'ResourcePage').objects.live()

        return context

    class Meta:
        label = 'Resources Cards Grid'
        admin_text = 'This block is configured in the MHO settings page.'
        icon = 'placeholder'
        template = 'patterns/organisms/grids/lean-cards.html'    