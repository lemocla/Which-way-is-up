"""
Views to manage artworks CRUD operations
"""
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from portfolio.models import Portfolio
from .models import ShopCategory, Artwork


def artworks(request):
    """
    View to return all artworks page
    """
    shop_category = None
    items = Artwork.objects.filter(display_shop=True,
                                   status="active").values()
    sort = None
    direction = None
    # current_sorting = 'None_None'

    if request.GET:
        if 'shop_category' in request.GET:
            shop_category = request.GET['shop_category']
            shop_category = ShopCategory.objects.filter(
                            backend_name=shop_category)[0]
            items = Artwork.objects.filter(shop_category=shop_category,
                                           display_shop=True,
                                           status="active").values()

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'
    print(current_sorting)

    context = {
        'category': shop_category,
        'artworks': items,
        'current_sorting': current_sorting
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """
    View portfolio detail
    """
    artwork = get_object_or_404(Artwork, id=artwork_id)
    related_items = Artwork.objects.filter(related_items=artwork.id)
    category = Portfolio.objects.get(artwork=artwork.id)

    context = {
        'artwork': artwork,
        'related_items': related_items,
        'category': category
    }

    return render(request, 'artworks/artwork_detail.html', context)
