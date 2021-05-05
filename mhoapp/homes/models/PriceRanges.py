from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel


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
    homes_search_page = ParentalKey(
        'wagtailcore.Page', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='homes_search_page'
    )

    # Editor panels configuration
    panels = [
        FieldPanel('type'),
        FieldPanel('price'),
        PageChooserPanel('homes_search_page', ['homes.HomesIndexPage']),
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

