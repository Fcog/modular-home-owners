from django.db import models
from wagtail.core.blocks import StreamBlock, MultipleChoiceBlock
from wagtail.images.blocks import ImageChooserBlock


class SectionBlock(StreamBlock):
    COLORS = [
        ('TRANSPARENT', 'transparent'),
        ('BLUE', 'blue'),
    ]

    background_image = ImageChooserBlock()
    background_color = MultipleChoiceBlock(
        choices=COLORS,
    )

    class Meta:
        icon = 'placeholder'