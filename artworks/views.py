"""
Views to manage artworks CRUD operations
"""

from django.shortcuts import render
from .models import ShopCategory


def artworks(request):
    """
    View to return all artworks page
    """
    shop_category = None

    if request.GET:
        if 'shop_category' in request.GET:
            shop_category = request.GET['shop_category']
            shop_category = ShopCategory.objects.filter(backend_name=shop_category)[0]

    context = {
        'category': shop_category,
    }

    return render(request, 'artworks/artworks.html', context)
