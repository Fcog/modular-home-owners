from django.apps import apps
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomesMap(blocks.StructBlock):
    map = ImageChooserBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        context['states'] = list(map(
            lambda item: {
                'name': item.title,
                'url': item.url,
            },
            context['page'].get_children().live().order_by('title')
        ))
        return context    

    class Meta:
        label = 'Homes Map'
        icon = 'placeholder'
        template = 'patterns/organisms/map/map.html'
