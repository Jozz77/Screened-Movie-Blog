from django import template

register = template.Library()

@register.filter(name='initials')
def initials(value):
    return value[0:1]