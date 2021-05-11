from django.db import models
from django.shortcuts import redirect
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    template = 'patterns/templates/forms/form_page.html'

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        MultiFieldPanel([
            InlinePanel('form_fields'),
        ], heading="Form Fields", classname="collapsible collapsed"),        
        MultiFieldPanel([
            FieldPanel('thank_you_text'),
        ], heading="Thank You Text", classname="collapsible collapsed"),                
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], heading="Email", classname="collapsible collapsed"),
    ]

    def get_landing_page_template(self, request):
        return 'patterns/templates/forms/thank-you.html'

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        source_page_id = request.POST.get('source-page-id')

        if source_page_id:
            source_page = Page.objects.get(pk=source_page_id)

            if source_page:
                request.session['form_page_success'] = True
                return redirect(source_page.url, permanent=False)

        # if no source_page is set, render default landing page
        return super().render_landing_page(request, form_submission, *args, **kwargs)