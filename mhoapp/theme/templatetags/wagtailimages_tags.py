from wagtail.images.templatetags.wagtailimages_tags import register
from pattern_library.monkey_utils import override_tag

# Overider the image tag in the templates used in the Pattern Library.
override_tag(register, name='image')