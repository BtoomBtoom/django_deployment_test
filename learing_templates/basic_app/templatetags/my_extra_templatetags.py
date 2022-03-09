from ast import arg
from django import template

register = template.Library()



@register.filter(name="replace_space_with_x")

def replace_space_with_x(text):
    return text.replace(" ",'x')

# @register.filter(name="x2")
def x(value,arg):
    return value*arg

register.filter('x',x)

