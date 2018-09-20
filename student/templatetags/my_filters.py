from django import template

register = template.Library()


@register.filter(name='range')
def times(number):
    return range(1, number+1)


@register.filter(name='times')
def times(number, t):
    result = t - number
    return range(result)


@register.filter(name='AB')
def ab(value):
    return ['A', 'B']
