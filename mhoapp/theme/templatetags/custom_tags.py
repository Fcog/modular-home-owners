from django import template

from mhoapp.base.models import HomePageSettings, BlocksSettings
from mhoapp.resources.models import ResourcePage

register = template.Library()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ in ['RadioSelect', 'CheckboxSelectMultiple', 'CheckboxInput']


@register.inclusion_tag('patterns/organisms/cta/links-list.html', takes_context=True)
def resources_cta(context, spacing):
    settings = BlocksSettings.for_request(context['request'])

    return {
        'text': settings.resources_text,                
        'links': ResourcePage.objects.live(),
        'spacing': spacing,
    }


@register.inclusion_tag('patterns/organisms/forms/form-modal.html', takes_context=True)
def form_modal(context, modal_id, form_id, form_height):
    request = context['request']  # important - you must have the request in context

    if not form_id:
        return context

    context['modal_id'] = modal_id
    context['form_id'] = form_id
    context['form_height'] = form_height

    return context