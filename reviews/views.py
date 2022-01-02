"""
Views for reviews app
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from artworks.models import Artwork
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from .models import Review
from .forms import ReviewForm


def all_reviews(request):
    """
    View to return the all the reviews page
    """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)


@login_required
def add_reviews(request, artwork_id, orderline_id):
    """
    View to return the all the reviews page
    """

    form = ReviewForm()
    artwork = Artwork.objects.get(id=artwork_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    order_line = None
    order = None

    if request.method == 'GET':
        if orderline_id:
            order_line = OrderLineItem.objects.get(id=orderline_id)
            order = Order.objects.get(id=order_line.order.id)

        if order.user_profile == user_profile and artwork == order_line.artwork:
            print('good to go')

        else:
            messages.error(request, 'You don\'t have the credentials to add a review for this item')
            return redirect('home')

    context = {
        'form': form,
        'artwork': artwork,
        'order_line': order_line,
        'user_profile': user_profile,
        'order': order
    }
    return render(request, 'reviews/add_reviews.html', context)
