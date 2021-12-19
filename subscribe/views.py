"""
Functions handling newsletter subscription
"""

from django.http import HttpResponseRedirect
from django.contrib import messages


def add_to_subscribe_list(request):
    """
    Add email to newsletter subscribe list
    Redirect to current page
    Display toast message
    """
    redirect_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        messages.success(request, 'Thank you for signing up to our '
                         'newsletter!')
    return HttpResponseRedirect(redirect_url)
