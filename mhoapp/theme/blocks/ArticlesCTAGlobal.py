from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock

from mhoapp.base.models import BlocksSettings


class ArticlesCTAGlobal(blocks.StructBlock):
    style = blocks.ChoiceBlock(choices=[
        ('blue', 'Blue'),
        ('white', 'White'),
    ], icon='snippet', default='blue')      

    add_border = blocks.BooleanBlock(default=True, required=False)      

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)

        context['links_style'] = 'green' if value['style'] == 'white' else 'blue'

        global_data = BlocksSettings.for_request(context['request'])

        context['introduction'] = global_data.art_cta_col_intro

        context['column_1_title'] = global_data.art_cta_col_1_title
        context['links_col_1'] = [
            global_data.art_cta_col_1_link_1,
            global_data.art_cta_col_1_link_2,
            global_data.art_cta_col_1_link_3,
            global_data.art_cta_col_1_link_4,
        ]

        context['column_2_title'] = global_data.art_cta_col_2_title
        context['links_col_2'] = [
            global_data.art_cta_col_2_link_1,
            global_data.art_cta_col_2_link_2,
            global_data.art_cta_col_2_link_3,
            global_data.art_cta_col_2_link_4,
        ]
        context['button_text'] = global_data.art_cta_button_text
        context['button_link'] = global_data.art_cta_button_link

        return context
    
    class Meta:
        label = 'Articles CTA (Global config)'
        icon = 'placeholder'
        template = 'patterns/organisms/text-links-button/text-links-button.html' 