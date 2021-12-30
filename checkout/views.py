"""
Views to handle checkout functionalities
"""
import json
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from bag.bag_contexts import bag_content
from profiles.models import UserProfile
from artworks.models import Artwork
from .models import Order, OrderLineItem
from .forms import OrderForm


def checkout(request):
    """
    Views to display checkout page
    """
    if request.method == 'POST':

        bag = request.session.get('bag', {})

        if request.POST.get('billing_same_as_delivery') == 'on':
            billing_street_address1 = request.POST['delivery_street_address1']
            billing_street_address2 = request.POST['delivery_street_address2']
            billing_town_or_city = request.POST['delivery_town_or_city']
            billing_postcode = request.POST['delivery_postcode']
            billing_county = request.POST['delivery_county']
            billing_country = request.POST['delivery_country']
        else:
            billing_street_address1 = request.POST['billing_street_address1']
            billing_street_address2 = request.POST['billing_street_address2']
            billing_town_or_city = request.POST['billing_town_or_city']
            billing_postcode = request.POST['billing_postcode']
            billing_county = request.POST['billing_county']
            billing_country = request.POST['billing_country']

        if request.POST.get('gift_option') == 'on':
            gift_option = True
        else:
            gift_option = False

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'delivery_street_address1': request.POST[
                                        'delivery_street_address1'],
            'delivery_street_address2': request.POST[
                                        'delivery_street_address2'],
            'delivery_town_or_city': request.POST['delivery_town_or_city'],
            'delivery_postcode': request.POST['delivery_postcode'],
            'delivery_county': request.POST['delivery_county'],
            'delivery_country': request.POST['delivery_country'],
            'billing_street_address1': billing_street_address1,
            'billing_street_address2': billing_street_address2,
            'billing_town_or_city': billing_town_or_city,
            'billing_postcode': billing_postcode,
            'billing_county': billing_county,
            'billing_country': billing_country,
            'gift_option': gift_option,
            'gift_message': request.POST['gift_message'],
            'gift_recipient': request.POST['gift_recipient'],
            'total': bag.grand_total
        }

        form = OrderForm(form_data)

        if form.is_valid():
            order = form.save(commit=False)
            order.bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    artwork = Artwork.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        artwork=artwork,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except ObjectDoesNotExist:
                    messages.error(request, (
                        "One of the artworks in your bag is not available. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            # emptpy bag
            del request.session['bag']
            if request.session.get('gift', {}):
                del request.session['gift']
            # message
            messages.success(request, f'Order successful - '
                             f'Order Number: {order.order_number}')
            # return home for now
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})

        if not bag:
            messages.error(request, 'There\'s nothing in your bag at the '
                           'moment')
            return redirect(reverse('shop'))

        current_bag = bag_content(request)
        is_gift = current_bag['is_gift']

        if str(is_gift) == 'on':
            is_gift_bool = True

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


def checkout_success(request, order_number):
    """
    Display when checkout is successful
    """
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
    }
    return render(request, 'checkout/checkout_success.html', context)