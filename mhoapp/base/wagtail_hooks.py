from wagtail.core import hooks
from wagtail.admin.menu import MenuItem
from django.templatetags.static import static
from django.utils.html import format_html


@hooks.register('register_settings_menu_item')
def register_forum_menu_item():
  return MenuItem('Forum', '/admin/forum', classnames='icon icon-group', order=10000)


@hooks.register('insert_global_admin_js', order=100)
def global_admin_js():
    return format_html(
        '<script src="{}"></script>',
        static('mhoapp/bundle.js')
    )  