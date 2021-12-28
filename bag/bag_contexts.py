"""
View to return  a context with all information needed to display the cart
"""

from django.shortcuts import get_object_or_404
from artworks.models import Artwork


def bag_content(request):
    """
    View to return shopping bag information into a dictionary
    """
    bag_items = []
    total = 0
    total_count = 0
    bag = request.session.get('bag', {})

    for artwork_id, artwork_data in bag.items():
        if isinstance(artwork_data, int):
            artwork = get_object_or_404(Artwork, pk=artwork_id)
            total += artwork_data * artwork.price
            total_count += artwork_data
            bag_items.append({
                'item_id': artwork_id,
                'quantity': artwork_data,
                'artwork': artwork,
            })
        else:
            artwork = get_object_or_404(Artwork, pk=artwork_id)
            for quantity in artwork_data.items():
                total += quantity * artwork.price
                total_count += quantity
                bag_items.append({
                    'artwork_id': artwork_id,
                    'quantity': quantity,
                    'artwork': artwork,
                })

    delivery = 0

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'total_count': total_count,
        'delivery': delivery,
        'grand_total': grand_total,
        }

    return context
