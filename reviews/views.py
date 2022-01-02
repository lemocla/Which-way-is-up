"""
Views for reviews app
"""

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
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

    user_profile = get_object_or_404(UserProfile, user=request.user)
    artwork = get_object_or_404(Artwork, id=artwork_id)
    order_line = None
    order = None

    if orderline_id:
        order_line = get_object_or_404(OrderLineItem, id=orderline_id)
        order = Order.objects.get(id=order_line.order.id)

    if request.method == 'POST':

        form_data = {
            'ratings': request.POST['ratings'],
            'comments': request.POST['comments'],
        }

        form = ReviewForm(form_data)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_profile = user_profile
            review.order_line = order_line
            review.artwork = artwork
            form.save()
            messages.success(request, f'Your review for {artwork.name} has '
                             f'been successfully added!')
            return redirect('order_history')

    else:
        review = Review.objects.filter(artwork=artwork)

        if review:
            messages.error(request, 'You\'ve already added a review for this'
                           ' item. You can edit your review')
            return redirect('order_history')

        if order.user_profile != user_profile or artwork != order_line.artwork:
            messages.error(request, 'You don\'t have the credentials to add a'
                           ' review for this item')
            return redirect('home')

        form = ReviewForm()

    context = {
        'form': form,
        'artwork': artwork,
        'order_line': order_line,
        'user_profile': user_profile,
        'order': order
    }
    return render(request, 'reviews/add_reviews.html', context)


@login_required
def edit_reviews(request, review_id):
    """
    View to return the all the reviews page
    """

    user_profile = get_object_or_404(UserProfile, user=request.user)
    review = get_object_or_404(Review, pk=review_id)

    redirect_url = request.POST.get('next', 'my_reviews')
    if user_profile.id != review.user_profile.id:
        messages.error(request, 'You don\'t have the credentials to add a'
                           ' review for this item')
        return redirect('home')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your review for {review.artwork.name}'
                             f' has been successfully edited!')
            return HttpResponseRedirect(redirect_url)

    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'reviews/edit_reviews.html', context)
