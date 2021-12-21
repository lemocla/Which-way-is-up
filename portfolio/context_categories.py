"""
Context to display subscribe form to all pages
"""

from .models import PortfolioCategory


def categories(request):
    """
    Put subscibe form in context
    """
    categories_object = PortfolioCategory.objects.all()
    cat = []
    for item in categories_object:
        cat.append(item.name)

    context = {'categories': cat}
    return context
