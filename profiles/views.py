"""
Views to render my profile page content
"""
from django.shortcuts import render, get_object_or_404, HttpResponse
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
    View and display the profile page
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
                subscribe = Mailing.objects.get(email=user.email)
                if not check:
                    subscribe.delete()
            except ObjectDoesNotExist:
                if check:
                    add = Mailing(email=user.email)
                    add.save()
            # Toast
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'We couldn\'t update your profile. '
                'Please check the form and try again.')
    else:
        form = UserProfileForm(instance=user_profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """
    A view to return a user's favourites
    """

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = user.wishlist_items.all()
    context = {
        'user': user,
        'wishlist': wishlist
    }

    return render(request, 'profiles/wishlist.html', context)


@login_required
def add_to_wishlist(request, artwork_id):
    """
    Add artwortk to user wishlist using ajax request
    """
    print(artwork_id)
    print(request.user)

    user = get_object_or_404(UserProfile, user=request.user)
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if user.wishlist_items.filter(pk=artwork_id).exists():
        # Toast
        messages.error(request, f'{artwork.name.capitalize()} already added '
                       'to wishlist')
    else:
        user.wishlist_items.add(artwork)
        messages.success(request, f'{artwork.name.capitalize()} added to '
                         'wishlist')

    return HttpResponse(status=200)


@login_required
def remove_from_wishlist(request, artwork_id):
    """
    Remove artwortk from user wishlist using ajax request
    """

    user = get_object_or_404(UserProfile, user=request.user)
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if user.wishlist_items.filter(pk=artwork_id).exists():
        user.wishlist_items.remove(artwork)
        messages.success(request, f'{artwork.name.capitalize()} successfully '
                         'removed from wishlist')
    else:
        # Toast
        messages.error(request, f'{artwork.name.capitalize()} is not '
                       'in your wishlit')

    return HttpResponse(status=200)


@login_required
def order_history(request):
    """
    A view to return a user's favourites
    """

    user = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=user).all()
    reviews = Review.objects.filter(user_profile=user).all()
    list_orderline = []

    for review in reviews:
        list_orderline.append(review.order_line.id)

    context = {
        'user': user,
        'orders': orders,
        'list_orderline': list_orderline
    }

    return render(request, 'profiles/order_history.html', context)
