import imp
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def modal_popup(url):
    return mark_safe(f"onclick=\"modalPopup('{url}')\"")
