from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def make_double_slash_single(value):
    # print("remove_comma_get_dot")
    if value and value != "None":
        value = value.replace("\\\\", "\\")
    return value