"""
Views for reviews application
"""

from django.shortcuts import render, redirect, get_object_or_404
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
    View to display all the reviews
    """
    reviews = Review.objects.all().order_by('-ratings', '-created_at')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)


@login_required
def add_reviews(request, artwork_id, orderline_id):
    """
    View to add a review to the database
    Display add a review page
    Check if artwork is active and if review has already been created
    """

    # Get user profile
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Get artwork
    artwork = get_object_or_404(Artwork, id=artwork_id)
    order_line = None
    order = None

    # Set redirect url
    redirect_url = request.GET.get('ref', 'my_reviews')

    # Check if artwork status is active
    if artwork.status != 'active':
        messages.error(request, 'Sorry you cannot leave a review for this'
                       ' item as it is no longer available.')
        return HttpResponseRedirect('order_history')

    # Check for existing reviews
    review = Review.objects.filter(artwork=artwork).filter(
             order_line=orderline_id)

    if review:
        messages.error(request, 'You\'ve already added a review for this'
                       ' item. You can edit your review')
        return redirect('order_history')

    # Check if review is added for a verified purchase
    if orderline_id:
        order_line = get_object_or_404(OrderLineItem, id=orderline_id)
        order = Order.objects.get(id=order_line.order.id)
        # Check if artwork and user profile match those of order lines
        if order.user_profile != user_profile or artwork != order_line.artwork:
            messages.error(request, 'You don\'t have the credentials to add a'
                           ' review for this item')
            return redirect('home')
    else:
        messages.error(request, 'You don\'t have the credentials to add a'
                       ' review for this item')
        return redirect('home')

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
            # Success message
            messages.success(request, f'Your review for '
                             f'{artwork.name.title()} has been '
                             f'successfully added!')
            return redirect(redirect_url)

    else:
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
    View to edit a review and display edit review page
    Check if authenticated user has created the review
    """

    # Get user profile
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Get review
    review = get_object_or_404(Review, pk=review_id)

    # Set redirect url
    redirect_url = request.GET.get('ref', 'my_reviews')

    # Check if authenticated user created review being deleted
    if user_profile.id != review.user_profile.id:
        messages.error(request, 'You don\'t have the credentials to edit a'
                       ' review for this item')
        return redirect('home')

    if request.method == 'POST':
        # Instanciate from with post data
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            # Save review with form data
            form.save()
            # message success
            messages.success(request, f'Your review for '
                             f'{review.artwork.name.title()} has been'
                             f' successfully edited!')
            return HttpResponseRedirect(redirect_url)

    else:
        # Instanciate form with review object
        form = ReviewForm(instance=review)
        # Info message
        messages.info(request, f'Editing review for {review.artwork.name}')

    # Set context
    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'reviews/edit_reviews.html', context)


@login_required
def delete_reviews(request, review_id):
    """
    View to delete a review
    Check if authenticated user created the review being deleted
    """

    # Get user profile
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Get review object
    review = get_object_or_404(Review, pk=review_id)

    # Get redirect url
    redirect_url = request.GET.get('next', 'my_reviews')

    # Check if authenticated user created review being deleted
    if user_profile.id != review.user_profile.id:
        messages.error(request, 'You don\'t have the credentials to delete a'
                       ' review for this item')
        return redirect('home')

    # Delete review
    review.delete()

    messages.success(request, 'Review successfully deleted!')
    return HttpResponseRedirect(redirect_url)
