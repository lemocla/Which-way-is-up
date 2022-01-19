"""
Views to handle shopping bag functionalities
"""

from django.shortcuts import (render, redirect, get_object_or_404,
                              HttpResponse, reverse)
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from artworks.models import Artwork


def view_bag(request):
    """
    View to return shopping bag page
    Remove out of stock and inactive items from bag
    """
    if request.session.get('bag'):
        bag = request.session['bag']
        for artwork_id in list(bag.keys()):
            try:
                artwork = Artwork.objects.get(id=artwork_id)
                # Out of stock items
                if artwork.stock == 0:
                    # Remove from bag
                    bag.pop(artwork_id)
                    # Update bag
                    request.session['bag'] = bag
                    # Error messages to infom user item not available
                    messages.error(request, f'{artwork.name.title()}'
                                   f' is out of stock and has been '
                                   f'removed from your bag.')
                # Draft and inactive artworks
                if artwork.status != 'active':
                    # Remove from bag
                    bag.pop(artwork_id)
                    # Update bag
                    request.session['bag'] = bag
                    # Message to inform user artwork is no longer available
                    messages.error(request, f'{artwork.name.title()}'
                                   f' is not longer available.')
            except ObjectDoesNotExist:
                # Remove from bag if artwork doesn't exist
                bag.pop(artwork_id)
                # Update bag
                request.session['bag'] = bag
                # Message to inform user artwork is no longer available
                messages.error(request, 'This artwork is no longer available')
        # Information message to users' about UK delivery only
        messages.info(request, 'Please note that we only deliver in the UK')

    return render(request, 'bag/bag.html')


def add_to_bag(request, artwork_id):
    """
    View to add a quantity of a specific item to the shopping bag
    """

    # Get artwork object
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    # Out of stock items
    if artwork.stock == 0 or artwork.status != 'active':
        messages.error(request, 'This item is not available for purchase.')
        return redirect(reverse('shop'))

    # Restrict adding items to bag to items displayed in shop
    if not artwork.display_shop:
        messages.error(request, 'This item is not available for purchase.')
        return redirect(reverse('shop'))

    # Set quantity to one when add to cart from shop
    if request.method == 'GET':
        quantity = 1
        redirect_url = request.META.get('HTTP_REFERER')

    # Set quantity when adding from artwork detail, wishlist and bag pages
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

    # Set redirect url to referrer
    redirect_url = request.META.get('HTTP_REFERER')

    bag = request.session.get('bag', {})

    # If bag exist, update bag else add to bag
    if str(artwork_id) in list(bag.keys()):
        # Update bag quantity
        bag[str(artwork_id)] += quantity
        # Success message
        messages.success(request, f'{artwork.name.title()}\'s quantity'
                         f' updated to {bag[str(artwork_id)]}.')
    else:
        # Add artwork id and quantity as key value to bag
        bag[artwork_id] = quantity
        # Success message
        messages.success(request, f'{artwork.name.title()} has been'
                         ' added to your bag.')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, artwork_id):
    """
    Adjust the quantity of a specified item to the specified amount
    """
    # Get artwork object
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    # Out of stock items
    if artwork.stock == 0 or artwork.status != 'active':
        # Error message
        messages.error(request, 'This item is not available for purchase.')
        # Redirect to shop
        return redirect(reverse('shop'))

    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    # Defensive design trying to update item not in shopping bag
    if artwork_id not in list(bag.keys()):
        messages.error(request, 'This item is not in your shopping bag')
        return redirect(reverse('shop'))

    # Update bag quantity else remove from bag
    if quantity > 0:
        bag[artwork_id] = quantity
        messages.success(request, f'{artwork.name.title()}\'s quantity '
                         f'updated to {bag[artwork_id]}.')
    else:
        bag.pop(artwork_id)
        messages.success(request, f'{artwork.name.title()} has been '
                         'removed from your bag.')

    request.session['bag'] = bag

    return HttpResponse(status=200)


def remove_from_bag(request, artwork_id):
    """Remove the item from the shopping bag"""

    try:
        # Get artwork object
        artwork = get_object_or_404(Artwork, pk=artwork_id)
        # Get bag from session
        bag = request.session.get('bag', {})

        # Defensive design trying to update item not in shopping bag
        if artwork_id not in list(bag.keys()):
            messages.error(request, 'This item is not in your shopping bag')
            return redirect(reverse('shop'))

        # remove artwork from shopping bag
        bag.pop(artwork_id)
        messages.success(request, f'{artwork.name.title()} has been '
                         'removed from your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except ObjectDoesNotExist:
        messages.error(request, 'Error removing item')
        return HttpResponse(status=500)


def gift_option(request):
    """
    Add / remove gift option in bag
    """
    is_gift = request.POST.get('is_gift')
    gift_message = request.POST.get('gift_message')

    # Initialize session
    gift = request.session.get('gift', {})

    # Gift option logic
    if is_gift == "on":
        gift[is_gift] = gift_message
        # Session is modified.
        request.session['gift'] = gift
    else:
        # Delete session
        if gift:
            del request.session['gift']

    return HttpResponse(status=200)
