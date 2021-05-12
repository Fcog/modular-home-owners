from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings
from mhoapp.resources.models import ResourcePage


class ResourcesCTA(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])

        context['text'] = global_data.resources_text                
        context['links'] = ResourcePage.objects.live()
        context['links_list_class'] = "pt-16 md:pt-44"

        return context

    class Meta:
        label = 'Resources CTA'
        admin_text = 'This block is configured in the MHO settings page.'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/links-list.html'

