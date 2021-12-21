"""
Views to handle display and portfolio management
"""
from django.shortcuts import render


def all(request):
    """
    View to return all page
    """
    return render(request, 'portfolio/all.html')