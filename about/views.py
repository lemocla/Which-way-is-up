"""
Views to render about page content
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def about(request):
    """
    View to return the about page
    """
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'about/about.html', context)


@login_required
def add_event(request):
    """
    Add portfolio to database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # Data from form
            form.save()
            messages.success(request, 'Event successfully added!')
            return redirect('about')
        else:
            messages.error(request, 'Event couldn\'t be added. '
                           'Please ensure the form is valid.')
    else:
        form = EventForm()

    context = {
        'form': form,
    }

    return render(request, "about/add_event.html", context)
