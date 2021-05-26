from django.apps import apps
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomesMap(blocks.StructBlock):
    map = ImageChooserBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        context['states'] = list(map(
            lambda item: item.name,
            apps.get_model('partners', 'LocationCategory').objects.filter(partnerpage__title__isnull=False).distinct()
        ))
        return context    

    class Meta:
        label = 'Homes Map'
        icon = 'placeholder'
        template = 'patterns/organisms/map/map.html'
