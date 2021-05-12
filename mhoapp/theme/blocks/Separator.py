from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class Separator(blocks.StaticBlock):
    class Meta:
        label = 'Block separator'
        icon = 'horizontalrule'
        template = 'patterns/atoms/separator/separator.html'    