"""
Views for Newsletter application
"""

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from profiles.models import UserProfile

from .forms import SubscribeForm


def add_to_mailing_list(request):
    """
    Add email to newsletter subscribe list
    Send acknowledgment email and display toast message
    Display toast message if email already in system
    Redirect to current page
    """
    redirect_url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':

        form = SubscribeForm(request.POST)

        if form.is_valid():
            # Data from form
            form.save()

            # Message / subject
            msg = 'Thank you for signing up to our newsletter!'
            # Acknowledgment email variables
            sender = settings.EMAIL_HOST_USER
            recipients = [form.cleaned_data['email_newsletter']]
            subject = msg
            body = render_to_string('newsletter/email/body.txt')

            # Check if email match a user and tick newsletter checkbox
            try:
                existing_user = User.objects.get(email=form.cleaned_data[
                                                'email_newsletter'])
            except ObjectDoesNotExist:
                existing_user = None

            if existing_user:
                profile = UserProfile.objects.get(user=existing_user)
                if profile and not profile.newsletter:
                    profile.newsletter = True
                    profile.save()
            # Toast message
            messages.success(request, msg)
            # Send mail
            try:
                send_mail(subject, body, sender, recipients)
            except BadHeaderError:
                messages.error(request, "Sorry - an error occured our side, "
                               "please retry later")
        else:
            # Error message
            messages.warning(request,
                             'You have already subscribed to our newsletter')
    return HttpResponseRedirect(redirect_url)
