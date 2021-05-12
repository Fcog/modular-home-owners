from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class LocationCategory(models.Model):
    # Database fields
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, default="")

    # Editor panels configuration
    panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel('name'),
                        FieldPanel('code'),
                    ]
                )
            ]
        )
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'locations of partners'
