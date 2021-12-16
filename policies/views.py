"""
Views to render policies content
"""

from django.shortcuts import render


def delivery_returns(request):
    """
    View to return delivery and returns policy
    """
    return render(request, 'policies/delivery_and_returns.html')


def terms_conditions(request):
    """
    View to return terms and conditions policy
    """
    return render(request, 'policies/terms_and_conditions.html')


def accessibility(request):
    """
    View to return accessibility policy
    """
    return render(request, 'policies/accessibility.html')


def privacy(request):
    """
    View to return privacy policy
    """
    return render(request, 'policies/privacy.html')
