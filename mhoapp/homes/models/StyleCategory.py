from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.core.models import Page


@register_snippet
class StyleCategory(models.Model):
    # Database fields
    name = models.CharField(max_length=255)
    style_page = models.ForeignKey(
        Page,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Editor panels configuration
    panels = [
        FieldPanel('name'),
        PageChooserPanel('style_page'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'styles of homes'