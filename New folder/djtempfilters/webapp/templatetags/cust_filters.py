from django import template

register=template.Library()

def clear(value):
    a=value[0:2]
    return a
register.filter('fc',clear)