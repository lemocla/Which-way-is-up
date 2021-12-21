"""
Views to render my profile page content
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
            form.save()
            messages.success(request, 'Profile updated successfully')
            # return HttpResponseRedirect('/my_profile/')
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
