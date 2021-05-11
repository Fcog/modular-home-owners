from wagtail.core import hooks
from wagtail.admin.menu import MenuItem


@hooks.register('register_settings_menu_item')
def register_forum_menu_item():
  return MenuItem('Forum', '/admin/forum', classnames='icon icon-group', order=10000)