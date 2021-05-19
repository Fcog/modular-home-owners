from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import ResourcePage


class ResourcesPageAdmin(ModelAdmin):
    model = ResourcePage
    menu_label = 'Resources'
    menu_icon = 'snippet'
    menu_order = 220
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    search_fields = ('title',)

modeladmin_register(ResourcesPageAdmin)
