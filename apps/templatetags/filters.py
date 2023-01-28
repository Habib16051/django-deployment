from django import template

register = template.Library()


def filters(value):
    return value + "This is a string from custom filter"


register.filter('custom_filters', filters)
