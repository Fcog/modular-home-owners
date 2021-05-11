from django import template

from mhoapp.base.models import HomePageSettings, BlocksSettings
from mhoapp.resources.models import ResourcePage

register = template.Library()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ in ['RadioSelect', 'CheckboxSelectMultiple', 'CheckboxInput']


@register.inclusion_tag('patterns/organisms/cta/links-list.html', takes_context=True)
def resources_cta(context, css_class):
    settings = BlocksSettings.for_request(context['request'])

    return {
        'text': settings.resources_text,                
        'links': ResourcePage.objects.live(),
        'links_list_class': css_class,
    }


@register.inclusion_tag('patterns/organisms/forms/form-modal.html', takes_context=True)
def form_modal(context, modal_id):
    request = context['request']  # important - you must have the request in context
    settings = HomePageSettings.for_request(request)
    form_page = settings.home_form

    if not form_page:
        return context

    form_page = form_page.specific

    # this will provide the parts needed to render the form
    # this does NOT handle the submission of the form - that still goes to the form page
    # this does NOT handle anything to do with rendering the 'thank you' message

    context['form_page'] = form_page
    context['modal_id'] = modal_id
    context['form'] = form_page.get_form(page=form_page, user=request.user)

    return context