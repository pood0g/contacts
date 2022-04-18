from django import template
from django.contrib.messages import constants

register = template.Library()

CLASS_LOOKUP_TABLE = {
    constants.DEBUG: "alert-warning",
    constants.INFO: "alert-info",
    constants.SUCCESS: "alert-success",
    constants.WARNING: "alert-warning",
    constants.ERROR: "alert-danger",
}

@register.simple_tag
def message_class(message):
    return CLASS_LOOKUP_TABLE[message.level]