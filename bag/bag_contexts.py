"""
View to return  a context with all information needed to display the cart
"""

from django.shortcuts import get_object_or_404
from artworks.models import Artwork
from profiles.models import UserProfile


def bag_content(request):
    """
    Return shopping bag information into a dictionary
    """
    bag_items = []
    total = 0
    total_count = 0
    bag = request.session.get('bag', {})

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)

    for artwork_id, artwork_data in bag.items():
        is_wishlist = False
        if isinstance(artwork_data, int):
            artwork = get_object_or_404(Artwork, pk=artwork_id)
            # price
            if artwork.on_sale:
                price = artwork.sale_price
            else:
                price = artwork.price
            # total and total count
            total += artwork_data * price
            total_count += artwork_data
            # wishlist items
            if request.user.is_authenticated:
                is_wishlist = user.wishlist_items.filter(
                              pk=artwork_id).exists()
            bag_items.append({
                'item_id': artwork_id,
                'quantity': artwork_data,
                'artwork': artwork,
                'is_wishlist': is_wishlist,
            })
        else:
            artwork = get_object_or_404(Artwork, pk=artwork_id)
            for quantity in artwork_data.items():
                # price
                if artwork.on_sale:
                    price = artwork.sale_price
                else:
                    price = artwork.price
                # total and total count
                total += quantity * artwork.price
                total_count += quantity
                # wishlist items
                if request.user.is_authenticated:
                    is_wishlist = user.wishlist_items.filter(
                                  pk=artwork_id).exists()
                bag_items.append({
                    'artwork_id': artwork_id,
                    'quantity': quantity,
                    'artwork': artwork,
                    'is_wishlist': is_wishlist,
                })

    # Gift option
    if request.session.get('gift'):
        for key, value in request.session['gift'].items():
            is_gift = key
            gift_message = value
    else:
        is_gift = None
        gift_message = None

    delivery = 0

    grand_total = total + delivery

    # Set context
    context = {
        'bag_items': bag_items,
        'total': total,
        'total_count': total_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'is_gift': is_gift,
        'gift_message': gift_message,
        }

    return context
