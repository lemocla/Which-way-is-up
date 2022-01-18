"""
Views to render contact form content
"""

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings

from django.contrib.auth.models import User
from profiles.models import UserProfile
from .forms import ContactForm


# https://docs.djangoproject.com/en/4.0/topics/forms/


def contact(request):
    """
    View to return the contact us page and create blank form
    Autofill form if user is authenticated but not super user
    Post request to send email to shop owner
    Send courtesy response to sender
    Display success message if the form is valid
    """
    # Process the form data when post
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # Data from form
            full_name = form.cleaned_data['full_name']
            sender = form.cleaned_data['email']
            recipients = [settings.EMAIL_HOST_USER]
            subject = form.cleaned_data['subject']
            body = render_to_string(
             'contact/email/email_body.txt',
             {'full_name': full_name, 'email': sender,
              'message': form.cleaned_data['message']}
            )

            # Courtesy email contstructor
            courtesy_subject = f"Your query: {subject}"
            courtesy_message = render_to_string(
             'contact/email/courtesy_body.txt', {'full_name': full_name})
            courtesy_sender = settings.EMAIL_HOST_USER
            courtesy_recipients = [sender]

            try:
                # Send mail
                send_mail(subject, body, sender, recipients)
                # send courtesy email to sender
                send_mail(courtesy_subject, courtesy_message, courtesy_sender,
                          courtesy_recipients)
                # display success message
                messages.success(request, 'Your message has been sent '
                                 'successfully! Thanks for your email')
            except BadHeaderError:
                messages.error(request, "Your message couldn't be sent")

            return redirect("contact")
    else:
        # Autofill user details if authenticated but not super user
        try:
            user = User.objects.get(username=request.user)
            user_profile = get_object_or_404(UserProfile, user=user)
            form = ContactForm(
                    initial={'email': user.email,
                             'full_name': user_profile.full_name,
                             })
        except ObjectDoesNotExist:
            form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
