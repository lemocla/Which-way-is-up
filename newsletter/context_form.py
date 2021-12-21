"""
Context to display subscribe form to all pages
"""

from .forms import SubscribeForm


def subscribe_form(request):
    """
    Put subscibe form in context
    """
    form = SubscribeForm()
    context = {'newsletter_form': form}
    return context
