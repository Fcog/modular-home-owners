from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import ArticlePage


class ArticlesAdmin(ModelAdmin):
    model = ArticlePage
    menu_label = 'Articles'
    menu_icon = 'pilcrow'
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    search_fields = ('title',)


modeladmin_register(ArticlesAdmin)