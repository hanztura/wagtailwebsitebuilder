from django import template

from home.helpers import json2obj

register = template.Library()


@register.filter
def json_to_object(data):
    return json2obj(data)
