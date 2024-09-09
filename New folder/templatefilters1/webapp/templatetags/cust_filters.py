from django import template
register=template.Library()

def test(value):
    result=value[0:5]
    return result
register.filter('t',test)

def integer(value):
    result=str(value)[0:2]
    return  result
register.filter('I',integer)