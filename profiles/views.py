"""
Views to render my profile page content
"""
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from newsletter.models import Mailing
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

    context = {
        'user': user,
    }

    return render(request, 'profiles/wishlist.html', context)
