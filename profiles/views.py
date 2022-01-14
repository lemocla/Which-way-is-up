"""
Views for profile application
"""

from django.shortcuts import (render, get_object_or_404, HttpResponse,
                              redirect, reverse)
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from newsletter.models import Mailing
from artworks.models import Artwork
from checkout.models import Order
from reviews.models import Review
from .models import UserProfile

from .forms import UserProfileForm


@login_required
def profile(request):
    """
    View to display the profile page
    Edit user profile information
    Add/remove email from newsletter according to choice
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            # Save form data in database
            form.save()
            # Add/ Remove email from newsletter if newsletter is true/false
            user = User.objects.get(username=user_profile)
            check = form.cleaned_data['newsletter']
            try:
                subscribe = Mailing.objects.get(email_newsletter=user.email)
                if not check:
                    subscribe.delete()
            except ObjectDoesNotExist:
                if check:
                    add = Mailing(email_newsletter=user.email)
                    add.save()
            # Toast success message
            messages.success(request, 'Profile updated successfully')
        else:
            # Toast error message
            messages.error(
                request,
                'We couldn\'t update your profile. '
                'Please check the form and try again.')
    else:
        # Instanciate form with user profile
        form = UserProfileForm(instance=user_profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def view_wishlist(request):
    """
    A view to return a user's favourites
    Get user and wishlist items
    """

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = user.wishlist_items.all()

    context = {
        'user': user,
        'wishlist': wishlist
    }

    return render(request, 'profiles/wishlist.html', context)


def add_to_wishlist(request, artwork_id):
    """
    Add artwortk to user wishlist using ajax request
    """
    if request.user.is_authenticated:
        # Get user
        user = get_object_or_404(UserProfile, user=request.user)
        # Get artwork
        artwork = get_object_or_404(Artwork, pk=artwork_id)

        # Restrict add to wishlist to active items
        if artwork.status != 'active':
            messages.error(request, 'This item is no longer available.')
            return redirect(reverse('shop'))

        # Check if items already added to wishlist
        if user.wishlist_items.filter(pk=artwork_id).exists():
            # Toast error message
            messages.error(request, f'{artwork.name.title()} already added '
                           'to wishlist')
        else:
            # Add to wishlist
            user.wishlist_items.add(artwork)
            # Toast success message
            messages.success(request, f'{artwork.name.title()} added to '
                             'wishlist')
    else:
        # Invite non authenticated users to login or register
        messages.info(request, ('Please login or create an account to add '
                      'items to your wishlist'))
    return HttpResponse(status=200)


@login_required
def remove_from_wishlist(request, artwork_id):
    """
    Remove artwortk from user wishlist using ajax request
    """
    # Get user
    user = get_object_or_404(UserProfile, user=request.user)
    # Get artwork
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    # Check if artwork in wishlist and remove
    if user.wishlist_items.filter(pk=artwork_id).exists():
        # Remove item from wishlist
        user.wishlist_items.remove(artwork)
        # Success message
        messages.success(request, f'{artwork.name.title()} successfully '
                         'removed from wishlist')
    else:
        # Toast error message
        messages.error(request, f'{artwork.name.title()} is not '
                       'in your wishlit')

    return HttpResponse(status=200)


@login_required
def order_history(request):
    """
    A view to return a user's order history
    Check purchase history for adding reviews
    """
    # Get user profile
    user = get_object_or_404(UserProfile, user=request.user)
    # Get orders for user
    orders = Order.objects.filter(user_profile=user).all().order_by('-date')
    # Get reviews for user
    reviews = Review.objects.filter(user_profile=user).all()
    list_orderline = []

    # Add existing reviews made against an order line
    for review in reviews:
        list_orderline.append(review.order_line.id)

    # Set context
    context = {
        'user': user,
        'orders': orders,
        'reviews': reviews,
        'list_orderline': list_orderline
    }

    return render(request, 'profiles/order_history.html', context)


@login_required
def my_reviews(request):
    """
    A view to return a user's reviews
    """

    # Get user profile
    user = get_object_or_404(UserProfile, user=request.user)
    # Get reviews for a user profile
    reviews = Review.objects.filter(user_profile=user).all().order_by(
              '-ratings', '-created_at')

    # Set context
    context = {
        'user': user,
        'reviews': reviews
    }

    return render(request, 'profiles/my_reviews.html', context)


@login_required
def order_details(request, order_number):
    """
    A view to display order details for a specific order
    """

    # Get user profile
    user = get_object_or_404(UserProfile, user=request.user)
    # Get order object
    order = get_object_or_404(Order, order_number=order_number)

    # Check that user match user in order object
    if user.id != order.user_profile.id:
        messages.error(request, 'You don\'t have the credentials to '
                       'access this page')

    # Set context
    context = {
        'order': order,
    }

    return render(request, 'profiles/order_detail.html', context)
