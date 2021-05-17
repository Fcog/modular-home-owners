from wagtail.core.models import Page


class PartnersIndexPage(Page):
    template = 'patterns/templates/flexible/two-col.html'

    # Parent page / subpage type rules
    subpage_types = ['PartnerTypePage']