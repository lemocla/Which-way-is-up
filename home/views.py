"""
Views to render homepage content
"""
from django.shortcuts import render


def index(request):
    """
    View to return the index page
    """
    return render(request, 'home/index.html')
