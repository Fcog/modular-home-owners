from django.db import models
from wagtail.core.models import Page


class ResourcesIndexPage(Page):
    template = 'patterns/templates/flexible/one-col.html'

    # Parent page / subpage type rules

    subpage_types = ['ResourcePage']


class ResourcePage(Page):
    template = 'patterns/templates/flexible/one-col.html'

    # Parent page / subpage type rules

    parent_page_types = ['ResourcesIndexPage']
