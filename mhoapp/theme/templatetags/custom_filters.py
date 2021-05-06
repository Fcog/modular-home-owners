
import math
from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

def currency(dollars):
    return "${:,}".format(dollars)

register.filter('currency', currency)

def truncate_float(value):
    if value.is_integer():
        return math.trunc(value)
    return value

register.filter('truncate_float', truncate_float)    

def remove_extension(value):
    base = os.path.basename(value)
    return os.path.splitext(base)[0]

register.filter('remove_extension', truncate_float)    