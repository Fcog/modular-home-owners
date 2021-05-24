from wagtail.core import blocks

from mhoapp.base.models import BlocksSettings


class FormBlock(blocks.StructBlock):
    form = blocks.PageChooserBlock(page_type="forms.FormPage", required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        request = context['request']
        page = value['form'].specific
        context['title'] = page.title
        context['form'] = page.get_form(page=value['form'], user=request.user)
        context['introduction'] = page.intro
        context['submit_button_text'] = page.submit_button_text
        context['form_page'] = value['form']
        return context

    class Meta:
        label = 'Form block'
        icon = 'placeholder'
        template = 'patterns/organisms/forms/form.html'