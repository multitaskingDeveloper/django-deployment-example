from django import template


register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    THIS FUNCTION CUTS OUT ALL OF 'arg' FROM THE STRING
    """

    return value.replace(arg, '')


# register.filter('cut', cut)
