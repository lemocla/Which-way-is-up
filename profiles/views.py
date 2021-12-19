"""
Views to render my profile page content
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """
    View to return the profile page
    """
    return render(request, 'profiles/profile.html')
