"""
Views to handle shopping bag functionalities
"""
from django.shortcuts import render, redirect, get_object_or_404
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

    if artwork_id in list(bag.keys()):
        bag[artwork_id] += quantity
        messages.success(request, f'Updated {artwork.name} quantity '
                         f'to {bag[artwork_id]}')
    else:
        bag[artwork_id] = quantity
        messages.success(request, f'Added {artwork.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
