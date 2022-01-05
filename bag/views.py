"""
Views to handle shopping bag functionalities
"""
from django.shortcuts import (render, redirect, get_object_or_404,
                              HttpResponse)
from django.contrib import messages
from artworks.models import Artwork


def bag(request):
    """
    View to return shopping bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, artwork_id):
    """
    Add a quantity of a specific item to the shopping bag
    """
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if request.method == 'GET':
        print("press add to cart button")
        quantity = 1
        redirect_url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

    redirect_url = request.META.get('HTTP_REFERER')

    bag = request.session.get('bag', {})

    if str(artwork_id) in list(bag.keys()):
        bag[str(artwork_id)] += quantity
        messages.success(request, f'{artwork.name.title()}\'s quantity'
                         f' updated to {bag[str(artwork_id)]}.')
    else:
        bag[artwork_id] = quantity
        messages.success(request, f'{artwork.name.title()} has been'
                         ' added to your bag.')

    request.session['bag'] = bag

    return redirect(redirect_url)


def ajdust_bag(request, artwork_id):
    """
    Adjust the quantity of a specified item to the specified amount
    """
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

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
        artwork = get_object_or_404(Artwork, pk=artwork_id)

        bag = request.session.get('bag', {})

        bag.pop(artwork_id)
        messages.success(request, f'{artwork.name.title()} has been '
                         'removed from your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def gift_option(request):
    """
    Add / remove gift option in bag
    """
    is_gift = request.POST.get('is_gift')
    gift_message = request.POST.get('gift_message')

    # initialize session
    gift = request.session.get('gift', {})

    # gift option logic
    if is_gift == "on":
        gift[is_gift] = gift_message
        # Session is modified.
        request.session['gift'] = gift
    else:
        # del session
        if gift:
            del request.session['gift']

    return HttpResponse(status=200)
