import imp
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
@stringfilter
def modal_popup(url, slug=None):
    return mark_safe(f"onclick=\"modalPopup('{url}', '{slug}')\"") if slug else mark_safe(f"onclick=\"modalPopup('{url}')\"")
