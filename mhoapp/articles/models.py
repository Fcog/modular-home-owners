from django.db import models
from wagtail.core.models import Page


class ArticlesIndexPage(Page):
    template = 'patterns/pages/archive/archive.html'

    # Parent page / subpage type rules

    subpage_types = ['ArticlePage']


class ArticlePage(Page):
    template = 'patterns/pages/articles/single.html'

    # Parent page / subpage type rules

    parent_page_types = ['ArticlesIndexPage']

