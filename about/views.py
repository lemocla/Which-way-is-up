"""
Views to manage About CRUD operations
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def about(request):
    """
    View to display the about page
    """
    # Get all events
    events = Event.objects.all()
    # Set context
    context = {
        'events': events,
    }
    return render(request, 'about/about.html', context)


@login_required
def add_event(request):
    """
    View to add an event entry to the database,
    Only accessible to the super user
    """
    # Security to restrict access to shop owner
    if not request.user.is_superuser:
        # Error message
        messages.error(request, 'Sorry, access restricted to the shop owner')
        # Redirect to homepage
        return redirect('home')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # Save form data
            form.save()
            # Display sucess message
            messages.success(request, 'Event successfully added!')
            return redirect('about')
        else:
            # Error message if form not valid
            messages.error(request, 'Event couldn\'t be added. '
                           'Please ensure the form is valid.')
    else:
        # Instanciate empty form
        form = EventForm()

    # Set context
    context = {
        'form': form,
    }

    return render(request, "about/add_event.html", context)


@login_required
def edit_event(request, event_id):
    """
    View to edit an event in the database
    """
    # Security to restrict access to shop owner
    if not request.user.is_superuser:
        # Error message
        messages.error(request, 'Sorry, access restricted to the shop owner')
        # Redirect home
        return redirect('home')

    # Get event object
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        # form instance with POST event data
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            # Save data from form
            form.save()
            # Success message
            messages.success(request, 'Event successfully updated!')
            # Redirect to about page
            return redirect('about')
        else:
            # Error message
            messages.error(request, 'The event couldn\'t be updated. '
                           'Please ensure the form is valid.')
    else:
        # Initiate form with event instance
        form = EventForm(instance=event)
        messages.info(request, f'Editing {event.place}')

    # Set context
    context = {
        'form': form,
        'event': event
    }

    return render(request, "about/edit_event.html", context)


@login_required
def delete_event(request, event_id):
    """
    View to delete an event from the database
    """
    # Restrict access to shop owner
    if not request.user.is_superuser:
        # Error message
        messages.error(request, 'Sorry, access restricted to the shop owner')
        # Redirect home
        return redirect('home')

    # Get event object
    event = get_object_or_404(Event, id=event_id)
    # Delete event
    event.delete()
    # Success message
    messages.success(request, 'Event successfully deleted!')

    return redirect('about')
