from django import template
register = template.Library()

def truncate5(value):

    result = value[:5]
    return result

@register.filter(name='t_n')
def truncate_n(value, n):

    result = value[:n]
    return result

register.filter('truncate5', truncate5)
