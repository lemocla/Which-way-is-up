"""
Views to render my profile page content
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    View and display the profile page
    """
    form = UserProfileForm()
    return render(request, 'profiles/profile.html', {'form': form})
