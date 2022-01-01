"""
Views for reviews app
"""

from django.shortcuts import render


def all_reviews(request):
    """
    View to return the all the reviews page
    """
    return render(request, 'reviews/reviews.html')
