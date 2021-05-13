from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

from mhoapp.base.utils import currency, truncate_float, remove_protocol


register = template.Library()

register.filter('currency', currency)
register.filter('truncate_float', truncate_float)    
register.filter('remove_protocol', remove_protocol)    
