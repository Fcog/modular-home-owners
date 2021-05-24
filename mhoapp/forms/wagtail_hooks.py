from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import FormPage


class FormPageAdmin(ModelAdmin):
    model = FormPage
    menu_label = 'Forms'
    menu_icon = 'form'
    menu_order = 230
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    search_fields = ('title',)

modeladmin_register(FormPageAdmin)