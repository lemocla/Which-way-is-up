"""
Views to render homepage content
"""

from django.shortcuts import render
from portfolio.models import Portfolio
from reviews.models import Review


def index(request):
    """
    View to display index page
    Get portfolio object to be displayed on homepage
    Get reviews to be displayed on homepage
    """

    # Get portfolio item
    portfolio_initial = Portfolio.objects.filter(homepage=True)
    if len(portfolio_initial) > 0:
        portfolio = portfolio_initial[0]
    else:
        portfolio = None

    # Get 3 latest top reviews
    # https://stackoverflow.com/questions/20555673/django-query-get-last-n-records
    reviews = Review.objects.all().order_by('-ratings', '-created_at')[:3]

    # Set context
    context = {
        'portfolio': portfolio,
        'reviews': reviews
    }

    return render(request, 'home/index.html', context)
