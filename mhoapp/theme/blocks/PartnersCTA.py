from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class PartnersCTA(blocks.StructBlock):
    style = blocks.ChoiceBlock(choices=[
        ('white', 'White'),
        ('gray', 'Gray'),
    ], icon='view', default='normal')     

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        context['style'] = value['style']

        global_data = BlocksSettings.for_request(context['request'])

        context['column_1_title'] = global_data.partner_1_title       
        context['column_1_text'] = global_data.partner_1_text     
        context['column_1_button_text'] = global_data.partner_1_button_text 
        context['column_1_button_url'] = global_data.partner_1_button_link.url     
        context['column_2_title'] = global_data.partner_2_title       
        context['column_2_text'] = global_data.partner_2_text        
        context['column_2_button_text'] = global_data.partner_2_button_text     
        context['column_2_button_url'] = global_data.partner_2_button_link.url                

        return context

    class Meta:
        label = 'Partners CTA'
        admin_text = 'This block is configured in the MHO settings page.'
        icon = 'placeholder'
        template = 'patterns/organisms/cta/double-column.html'

