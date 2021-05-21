from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class GetYourHouseCTA(blocks.StructBlock):
    style = blocks.ChoiceBlock(choices=[
        ('blue', 'Blue'),
        ('dark-blue', 'Dark Blue'),
    ], icon='view', default='blue')  

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        context['style'] = value['style']

        global_data = BlocksSettings.for_request(context['request'])

        context['title'] = global_data.gyh_title        
        context['column_1_title'] = global_data.gyh_column_1_title        
        context['column_1_text'] = global_data.gyh_column_1_text         
        context['column_2_title'] = global_data.gyh_column_2_title        
        context['column_2_text'] = global_data.gyh_column_2_text         
        context['column_3_title'] = global_data.gyh_column_3_title        
        context['column_3_text'] = global_data.gyh_column_3_text     
        context['link_1_text'] = global_data.gyh_link_1_text     
        context['link_1_url'] = global_data.gyh_link_1_link.url
        context['link_2_text'] = global_data.gyh_link_2_text     
        context['link_2_url'] = global_data.gyh_link_2_link.url

        return context

    class Meta:
        label = 'Get Your House CTA'
        icon = 'placeholder'
        admin_text = 'This block is configured in the MHO settings page.'
        template = 'patterns/organisms/cta/icons-cols.html'

