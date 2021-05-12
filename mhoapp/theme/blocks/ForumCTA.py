from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class ForumCTA(blocks.StaticBlock):
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        global_data = BlocksSettings.for_request(context['request'])

        context['title'] = global_data.forum_title
        context['text'] = global_data.forum_text
        context['button_text'] = global_data.forum_button_text
        context['button_url'] = global_data.forum_button_url()

        return context

    class Meta:
        label = 'Forum CTA'
        icon = 'placeholder'
        admin_text = 'This block is configured in the MHO settings page.'
        template = 'patterns/organisms/cta/cta.html'

