"""
Views to render homepage content
"""
from django.shortcuts import render

from portfolio.models import Portfolio


def index(request):
    """
    View to return the index page
    """
    portfolio = Portfolio.objects.filter(
                homepage=True)[0]
    context = {
        'portfolio': portfolio
    }
    return render(request, 'home/index.html', context)
