from wagtail.core.models import Page


class PartnersIndexPage(Page):
    template = 'patterns/templates/archive/archive.html'

    # Parent page / subpage type rules
    subpage_types = ['PartnerTypePage']