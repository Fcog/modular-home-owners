from wagtail.admin.forms import WagtailAdminPageForm


# Register your models here.
class HomePageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Manually edit the default form's title attributes:
        title = self.fields['title']
        title.label = 'Home name'