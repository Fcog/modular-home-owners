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
    # Database fields
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    submit_button_text = models.CharField(max_length=120, blank=True, default="Send")

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        MultiFieldPanel([
                FieldPanel('intro', classname="full"),
                FieldPanel('submit_button_text', classname="full"),
        ], heading="Texts", classname="collapsible collapsed"),     
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['paragraph'] = self.thank_you_text

        return context

    def get_template(self, request):
        if request.htmx:
            return 'patterns/molecules/forms/form-body.html'
        
        return 'patterns/templates/forms/form-page.html'       

    def get_landing_page_template(self, request):
        if request.htmx:
            return 'patterns/atoms/paragraph/paragraph.html'

        return 'patterns/templates/forms/thank-you.html'

    class Meta:
        verbose_name = "Form"    