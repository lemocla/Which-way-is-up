"""
Views to render contact form content
"""
from django.shortcuts import render


def contact(request):
    """
    View to return the contact us page
    """
    return render(request, 'contact/contact.html')
