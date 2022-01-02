"""
Views for reviews app
"""

from django.shortcuts import render
from .models import Review

def all_reviews(request):
    """
    View to return the all the reviews page
    """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)
