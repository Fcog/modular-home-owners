from django.apps import apps
from wagtail.core import blocks
from wagtail_link_block.blocks import LinkBlock


class PopularHomesGrid(blocks.StructBlock):
    title = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = LinkBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)

        context['button_url'] = value['button_link'].get_url

        context['homes'] = apps.get_model('homes', 'HomePage').objects.live().order_by('-hit_count_generic__hits')[:6]

        context['homes_grid_class'] = "pb-20 md:pb-36"

        return context

    class Meta:
        label = 'Popular Homes Grid'
        icon = 'placeholder'
        template = 'patterns/organisms/homes-grid/homes-grid.html'
       
