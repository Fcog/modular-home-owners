from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import PartnerPage


class PartnersPageAdmin(ModelAdmin):
    model = PartnerPage
    menu_label = 'Partners'
    menu_icon = 'snippet'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name',)
    search_fields = ('name',)


modeladmin_register(PartnersPageAdmin)
