"""
Context to display subscribe form to all pages
"""

from .models import ShopCategory


def shop_categories(request):
    """
    Build a dictionary to use for navigation in base.html
    Put the dictionary in the context
    """
    shop_object = ShopCategory.objects.all()
    shop = []
    for item in shop_object:
        shop.append(item)

    context = {'shop_categories': shop, 'request': request}

    return context
