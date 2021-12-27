"""
Views to manage artworks CRUD operations
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from portfolio.models import Portfolio
from .models import ShopCategory, Artwork
from .forms import ArtworkForm


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
    if artwork.portfolio:
        category = Portfolio.objects.get(artwork=artwork.id)
    else:
        category = None

    context = {
        'artwork': artwork,
        'related_items': related_items,
        'category': category
    }

    return render(request, 'artworks/artwork_detail.html', context)


@login_required
def add_artwork(request):
    """
    Add artwork to database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect(reverse('home'))

    if request.method == 'POST':

        form = ArtworkForm(request.POST, request.FILES)

        if form.is_valid():
            # Data from form
            artwork = form.save()
            messages.success(request, 'Artwork successfully added!')
            return redirect(reverse('artwork_details', args=[artwork.id]))
        else:
            messages.error(request, 'Artwork couldn\'t be added. '
                           'Please ensure the form is valid.')
    else:
        form = ArtworkForm()

    context = {
        'form': form,
    }

    return render(request, "artworks/add_artwork.html", context)


@login_required
def edit_artwork(request, artwork_id):
    """
    Edit artwork in the database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect(reverse('home'))

    artwork = get_object_or_404(Artwork, id=artwork_id)

    if request.method == 'POST':

        form = ArtworkForm(request.POST, request.FILES, instance=artwork)

        if form.is_valid():
            # Data from form
            form.save()
            messages.success(request, 'Artwork successfully updated!')
            return redirect(reverse('artwork_details', args=[artwork.id]))
        else:
            messages.error(request, 'Portfolio couldn\'t be updated. '
                           'Please ensure the form is valid.')
    else:
        form = ArtworkForm(instance=artwork)
        messages.info(request, f'Editing {artwork.name}')

    context = {
        'form': form,
        'artwork': artwork
    }

    return render(request, "artworks/edit_artwork.html", context)
