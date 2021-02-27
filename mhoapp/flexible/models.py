from django.db import models
from wagtail.core.models import Page


class FlexibleOneColumnPage(Page):
    template = 'patterns/pages/flexible/one-col.html'


class FlexibleTwoColumnPage(Page):
    template = 'patterns/pages/flexible/two-col.html'
