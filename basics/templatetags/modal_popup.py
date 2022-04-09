import imp
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
@stringfilter
def modal_popup(value):
    return mark_safe(f"onclick='modalPopup({value})'")
