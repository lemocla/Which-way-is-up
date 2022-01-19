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
    View to display artworks page (shop)
    """
    shop_category = None
    items = Artwork.objects.filter(display_shop=True,
                                   status="active").values()
    sort = None
    direction = None
    user = None
    wishlist = None

    # Get wishlist items for authenticated users
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = user.wishlist_items.values()

    if request.GET:
        # Filter artworks by shop category name
        if 'shop_category' in request.GET:
            shop_category = request.GET['shop_category']
            # Sale shop category
            if shop_category == 'sale':
                shop_category = 'sale'
                items = Artwork.objects.filter(on_sale=True,
                                               display_shop=True,
                                               status="active").values()
            else:
                # Shop categories from database
                shop_category = ShopCategory.objects.filter(
                                backend_name=shop_category)[0]
                items = Artwork.objects.filter(shop_category=shop_category,
                                               display_shop=True,
                                               status="active").values()

        # Sort artworks according to value in sort select field
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

    # Set sorting variable
    current_sorting = f'{sort}_{direction}'

    # Set context
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
    View to display artworks' detail
    Restrict user's access to draft and inactive items
    """

    artwork = get_object_or_404(Artwork, id=artwork_id)
    related_items = Artwork.objects.filter(related_items=artwork.id)
    user = None
    wishlist = None
    is_wishlist = None
    reviews = Review.objects.filter(artwork=artwork.id).order_by(
              '-ratings', '-created_at')
    orderlist = []
    order_line_add = None

    # restrict access to draft/inactive artwork
    if artwork.status != 'active':
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, access restricted to the shop '
                           'owner')
            return redirect(reverse('home'))

    # get wishlist items and first order line for adding reviews
    if request.user.is_authenticated:
        # Get user
        user = get_object_or_404(UserProfile, user=request.user)
        # Get wishlist
        wishlist = user.wishlist_items.all()
        is_wishlist = user.wishlist_items.filter(pk=artwork_id).exists()
        # Get user's orders
        orders = Order.objects.filter(user_profile=user)
        # Append order list to check for reviews
        for line in reviews:
            orderlist.append(line.order_line.id)
        # Filter order lines for artwork where reviews had not been added
        order_line_add = OrderLineItem.objects.filter(
                         order_id__in=orders).filter(artwork=artwork).exclude(
                         id__in=orderlist).first()

    # Get portfolio object
    if artwork.portfolio:
        category = Portfolio.objects.get(artwork=artwork.id)
    else:
        category = None

    if artwork.display_shop:
        shop_category = ShopCategory.objects.get(artwork=artwork.id)
    else:
        shop_category = None

    # Set context
    context = {
        'artwork': artwork,
        'related_items': related_items,
        'category': category,
        'shop_category': shop_category,
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
    View to add an artwork entry to the database
    Display add artwork template
    Restrict access to superuser
    """
    # Restrict access to shop owner
    if not request.user.is_superuser:
        # Error message
        messages.error(request, 'Sorry, access restricted to the shop owner')
        # Redirect to homepage
        return redirect(reverse('home'))

    if request.method == 'POST':
        # Instanciate form with form data and files
        form = ArtworkForm(request.POST, request.FILES)

        if form.is_valid():
            # Save data from form
            artwork = form.save()
            # Success message
            messages.success(request, 'Artwork successfully added!')
            # Redirect to artwork detail page
            return redirect(reverse('artwork_details', args=[artwork.id]))
        else:
            # Error message if form not valid
            messages.error(request, 'Artwork couldn\'t be added. '
                           'Please ensure the form is valid.')
    else:
        # Instanciate empty form
        form = ArtworkForm()

    # Set context
    context = {
        'form': form,
    }

    return render(request, "artworks/add_artwork.html", context)


@login_required
def edit_artwork(request, artwork_id):
    """
    View to edit artwork in the database
    Display edit artwork page
    Restrict access to super user
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to the shop owner')
        return redirect(reverse('home'))

    # Get artwork object
    artwork = get_object_or_404(Artwork, id=artwork_id)

    if request.method == 'POST':
        # Instanciate form with post data and files
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            # Save data from form
            form.save()
            # Message success
            messages.success(request, 'Artwork successfully updated!')
            return redirect(reverse('artwork_details', args=[artwork.id]))
        else:
            # Error message
            messages.error(request, 'Artwork couldn\'t be updated. '
                           'Please ensure the form is valid.')
    else:
        # Instanciate form with artwork object data
        form = ArtworkForm(instance=artwork)
        # Info message
        messages.info(request, f'Editing {artwork.name}')

    # set context
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
        messages.error(request, 'Sorry, access restricted to the shop owner')
        return redirect(reverse('home'))

    # Set redirect url
    if 'ref' in request.GET:
        redirect_url = request.GET['ref']
    else:
        redirect_url = request.META.get('HTTP_REFERER', '')

    # Get artwork object
    artwork = get_object_or_404(Artwork, id=artwork_id)
    # Delete artwork
    artwork.post_delete()

    # Info message if items set inactive during delete method
    if artwork.lineartworks.exists():
        messages.info(request, 'This item has been set has inactive, as there '
                      'are orders attached to it')
    else:
        # Success message if artwork deleted
        messages.success(request, 'Artwork successfully deleted!')

    return HttpResponseRedirect(redirect_url)
