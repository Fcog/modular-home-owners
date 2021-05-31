from django.apps import apps
from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class ResourcesCTA(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])

        context['text'] = global_data.resources_text                
        context['links'] = apps.get_model('resources', 'ResourcePage').objects.live()
        context['spacing'] = 'big'

        return context

    class Meta:
        label = 'Resources Links'
        admin_text = 'This block is configured in the MHO settings page.'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/links-list.html'

