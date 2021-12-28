"""
Views to handle shopping bag functionalities
"""
from django.shortcuts import render


def bag(request):
    """
    View to return shopping bag page
    """
    return render(request, 'bag/bag.html')
