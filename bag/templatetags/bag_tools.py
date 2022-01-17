"""
Template tags
"""
from datetime import date, timedelta
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate subtotal
    """
    return price * quantity


# https://stackoverflow.com/questions/19598213/generating-a-date-relative-to-another-date-in-django-template
@register.filter(name='calc_est_delivery')
def plus_days(days):
    """
    Calculate estimated delivery day
    """
    return date.today() + timedelta(days=days)
