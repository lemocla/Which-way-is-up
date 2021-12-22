"""
Views to manage artworks CRUD operations
"""

from django.shortcuts import render


# Create your views here.
def artworks(request):
    """
    View to return all artworks page
    """
    return render(request, 'artworks/artworks.html')

