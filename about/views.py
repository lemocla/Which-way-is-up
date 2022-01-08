"""
Views to render about page content
"""
from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect('home')

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


@login_required
def edit_event(request, event_id):
    """
    Edit portfolio in the database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect('home')

    event = get_object_or_404(Event, id=event_id)
    # event.date_start = datetime.strftime(event.date_start, '%Y-%m-%d')
    # event.save()
    if request.method == 'POST':

        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            # Data from form
            form.save()
            messages.success(request, 'Event successfully updated!')
            return redirect('about')
        else:
            messages.error(request, 'The event couldn\'t be updated. '
                           'Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'Editing {event.place}')

    context = {
        'form': form,
        'event': event
    }

    return render(request, "about/edit_event.html", context)


@login_required
def delete_event(request, event_id):
    """
    Delete portfolio from the database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect('home')

    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, 'Event successfully deleted!')
    return redirect('about')
