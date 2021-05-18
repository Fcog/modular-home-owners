from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageCaption(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    caption = blocks.TextBlock(default='')

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context    

    class Meta:
        icon = 'image'
        label = 'Image'
        template = 'patterns/molecules/images/image-caption.html'    