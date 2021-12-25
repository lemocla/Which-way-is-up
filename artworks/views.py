"""
Views to manage artworks CRUD operations
"""
from django.shortcuts import render

from .models import ShopCategory, Artwork


def artworks(request):
    """
    View to return all artworks page
    """
    shop_category = None
    items = Artwork.objects.filter(display_shop=True,
                                   status="active")

    if request.GET:
        if 'shop_category' in request.GET:
            shop_category = request.GET['shop_category']
            shop_category = ShopCategory.objects.filter(
                            backend_name=shop_category)[0]
            items = Artwork.objects.filter(shop_category=shop_category,
                                           display_shop=True,
                                           status="active")

    context = {
        'category': shop_category,
        'artworks': items
    }

    return render(request, 'artworks/artworks.html', context)
