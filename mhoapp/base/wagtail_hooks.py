from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import MHOSettings


class MHOSettingsAdmin(ModelAdmin):
    model = MHOSettings
    menu_label = 'MHO'
    menu_icon = 'clipboard-list'
    menu_order = 1100
    add_to_settings_menu = True
    exclude_from_explorer = False


modeladmin_register(MHOSettingsAdmin)
