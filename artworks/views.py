"""
Views to manage artworks CRUD operations
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from portfolio.models import Portfolio
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from reviews.models import Review
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
    user = None
    wishlist = None

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = user.wishlist_items.values()

    if request.GET:
        if 'shop_category' in request.GET:
            shop_category = request.GET['shop_category']
            if shop_category == 'sale':
                shop_category = 'sale'
                items = Artwork.objects.filter(on_sale=True,
                                               display_shop=True,
                                               status="active").values()
            else:
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

    context = {
        'category': shop_category,
        'artworks': items,
        'current_sorting': current_sorting,
        'user': user,
        'wishlist': wishlist
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """
    View artwork detail
    Restrict user's access to active items
    """
    artwork = get_object_or_404(Artwork, id=artwork_id)
    related_items = Artwork.objects.filter(related_items=artwork.id)
    user = None
    wishlist = None
    is_wishlist = None
    reviews = Review.objects.filter(artwork=artwork.id)
    orderlist = []
    order_line_add = None

    # restrict access to draft/inactive artwork
    if artwork.status != 'active':
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, access restricted to shop owner')
            return redirect(reverse('home'))

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = user.wishlist_items.all()
        is_wishlist = user.wishlist_items.filter(pk=artwork_id).exists()
        orders = Order.objects.filter(user_profile=user)
        for line in reviews:
            orderlist.append(line.order_line.id)
        order_line_add = OrderLineItem.objects.filter(
                         order_id__in=orders).filter(artwork=artwork).exclude(
                         id__in=orderlist).first()

    if artwork.portfolio:
        category = Portfolio.objects.get(artwork=artwork.id)
    else:
        category = None

    context = {
        'artwork': artwork,
        'related_items': related_items,
        'category': category,
        'user': user,
        'wishlist': wishlist,
        'is_wishlist': is_wishlist,
        'reviews': reviews,
        'order_line_add': order_line_add,
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
            # If status is not active, remove from wishlist
            if artwork.status != 'active':
                users_wishlist = UserProfile.objects.filter(
                                 wishlist_items=artwork_id)
                for profile in users_wishlist:
                    profile.wishlist_items.remove(artwork_id)
                    profile.save()
            messages.success(request, 'Artwork successfully updated!')
            return redirect(reverse('artwork_details', args=[artwork.id]))
        else:
            messages.error(request, 'Artwork couldn\'t be updated. '
                           'Please ensure the form is valid.')
    else:
        form = ArtworkForm(instance=artwork)
        messages.info(request, f'Editing {artwork.name}')

    context = {
        'form': form,
        'artwork': artwork
    }

    return render(request, "artworks/edit_artwork.html", context)


@login_required
def delete_artwork(request, artwork_id):
    """
    Delete artwork from the database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect(reverse('home'))

    # Redirect url
    if 'ref' in request.GET:
        redirect_url = request.GET['ref']
    else:
        redirect_url = request.META.get('HTTP_REFERER')

    artwork = get_object_or_404(Artwork, id=artwork_id)
    artwork.delete()
    messages.success(request, 'Artwork successfully deleted!')
    return HttpResponseRedirect(redirect_url)
