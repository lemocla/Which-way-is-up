"""
Context to display subscribe form to all pages
"""

from .models import PortfolioCategory, Portfolio


def categories(request):
    """
    Build a dictionary to use for navigation in base.html
    Put the dictionary in the context
    """
    categories_object = PortfolioCategory.objects.all()
    portfolio_object = Portfolio.objects.all()
    cat = []
    for item in categories_object:
        portfolio_object = Portfolio.objects.filter(category=item.id)
        portfolio_list = []
        # get portfolio for category item
        for portfolio in portfolio_object:
            portfolio_list.append(portfolio)
        # build dictionary for navigation in base.html
        dic = {'name': item.name, 'id': item.id, 'col': portfolio_list}
        cat.append(dic)

    context = {'categories': cat}
    return context
