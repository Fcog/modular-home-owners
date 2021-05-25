from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class FormBlock(blocks.StructBlock):
    form_id = blocks.CharBlock()
    form_height = blocks.IntegerBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context.update(value)
        return context

    class Meta:
        label = 'Form block'
        icon = 'placeholder'
        template = 'patterns/organisms/forms/wufoo.html'