"""
Views to render contact form content
"""
from django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm

# https://docs.djangoproject.com/en/4.0/topics/forms/


def contact(request):
    """
    View to return the contact us page and create blank form
    Post request to send email to shop owner
    Display success message if the form is valid
    """
    # Process the form data when post
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # display success message
            messages.success(request, 'Your message has been sent '
                             'successfully! Thanks for your email')
            form = ContactForm()
    # create a blank form
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
