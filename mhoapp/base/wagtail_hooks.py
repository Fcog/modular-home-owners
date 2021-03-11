from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
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


@hooks.register('register_settings_menu_item')
def register_forum_menu_item():
  return MenuItem('Forum', '/admin/forum', classnames='icon icon-group', order=10000)