from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel


@register_snippet
class StyleCategory(models.Model):
    # Database fields
    name = models.CharField(max_length=255)

    # Editor panels configuration
    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'styles of homes'