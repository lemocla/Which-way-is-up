"""
Views to render my profile page content
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import DeliveryForm, ContactDetailsForm

@login_required
def profile(request):
    """
    View to return the profile page
    """
    del_form = DeliveryForm()
    cont_form = ContactDetailsForm()
    return render(request, 'profiles/profile.html', {'del_form': del_form, 'cont_form': cont_form})
