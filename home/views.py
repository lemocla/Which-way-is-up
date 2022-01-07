"""
Views to render homepage content
"""
from django.shortcuts import render

from portfolio.models import Portfolio
from reviews.models import Review


def index(request):
    """
    View to return the index page
    """
    portfolio = Portfolio.objects.filter(
                homepage=True)[0]
    # https://stackoverflow.com/questions/20555673/django-query-get-last-n-records
    reviews = Review.objects.all().order_by('-ratings', '-created_at')[:3]
    context = {
        'portfolio': portfolio,
        'reviews': reviews
    }

    return render(request, 'home/index.html', context)
