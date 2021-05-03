from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import HomePage


class HomesAdmin(ModelAdmin):
    model = HomePage
    menu_label = 'Homes'
    menu_icon = 'home'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title','code','bedrooms','baths','sqft','cost','estimated_cost','verified')
    search_fields = ('title',)


modeladmin_register(HomesAdmin)
