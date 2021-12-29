"""
Views to handle checkout functionalities
"""
from django.shortcuts import render


def checkout(request):
    """
    Views to display checkout page
    """
    return render(request, 'checkout/checkout.html')
