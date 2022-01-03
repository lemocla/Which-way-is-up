from django import template
from datetime import date, timedelta

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


# https://stackoverflow.com/questions/19598213/generating-a-date-relative-to-another-date-in-django-template
@register.filter(name='calc_est_delivery')
def plus_days(days):
    return date.today() + timedelta(days=days)
