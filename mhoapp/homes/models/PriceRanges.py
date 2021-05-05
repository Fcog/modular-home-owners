from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel


@register_snippet
class PriceRanges(models.Model):
    UNDER = 'UN'
    OVER = 'OV'

    # Database fields
    type = models.CharField(
        max_length=2,
        choices=[
            (UNDER, 'Under'),
            (OVER, 'Over'),
        ],
        default=UNDER,
    )
    price = models.PositiveIntegerField(default=0)

    # Editor panels configuration
    panels = [
        FieldPanel('type'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return self.get_type_display() + ' ' + str(self.price)

    def get_min_price_range(self):
        if self.type == self.UNDER:
            return None
        return self.price

    def get_max_price_range(self):
        if self.type == self.UNDER:
            return self.price
        return None

    class Meta:
        verbose_name_plural = 'price ranges'

