"""
Views to handle checkout functionalities
"""
from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from bag.bag_contexts import bag_content
from profiles.models import UserProfile
from .forms import OrderForm


def checkout(request):
    """
    Views to display checkout page
    """
    if request.method == 'GET':
        bag = request.session.get('bag', {})

        if not bag:
            messages.error(request, 'There\'s nothing in your bag at the '
                           'moment')
            return redirect(reverse('shop'))

        current_bag = bag_content(request)
        is_gift = current_bag['is_gift']
        print(is_gift)
        if str(is_gift) == 'on':
            is_gift_bool = True
            print('it true')
        else:
            is_gift_bool = False
        gift_message = current_bag['gift_message']

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = OrderForm(initial={
                    'full_name': profile.full_name,
                    'email': profile.user.email,
                    'phone_number': profile.phone_number,
                    'delivery_street_address1': profile.street_address1,
                    'delivery_street_address2': profile.street_address2,
                    'delivery_county': profile.county,
                    'delivery_postcode': profile.postcode,
                    'delivery_town_or_city': profile.town_or_city,
                    'delivery_country': profile.country,
                    'billing_street_address1': profile.street_address1,
                    'billing_street_address2': profile.street_address2,
                    'billing_county': profile.county,
                    'billing_postcode': profile.postcode,
                    'billing_town_or_city': profile.town_or_city,
                    'billing_country': profile.country,
                    'is_gift': is_gift_bool,
                    'gift_message': gift_message
                })
            except ObjectDoesNotExist:
                form = OrderForm()
        else:
            form = OrderForm()
    context = {
        "form": form,
    }
    return render(request, 'checkout/checkout.html', context)
