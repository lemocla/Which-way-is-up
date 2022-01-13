"""
Forms configuration for Checkout application
"""

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Configure form to collect order details during checkout
    """
    class Meta:
        """
        Define form meta properties
        """
        model = Order
        exclude = ('order_number', 'date', 'bag',
                   'user_profile', 'total', 'status',
                   'paid', 'transaction_id')
        widgets = {
          'gift_message': forms.Textarea(attrs={'rows': 4, }),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'gift_recipient': 'Enter gift recipient',
            'gift_message': ('Enter your gift message - make sure to '
                             'include to / from names'),
            'delivery_street_address1': 'Street Address 1',
            'delivery_street_address2': 'Street Address 2',
            'delivery_town_or_city': 'Town or City',
            'delivery_postcode': 'Postal Code',
            'delivery_county': 'County, State or Locality',
            'billing_street_address1': 'Street Address 1',
            'billing_street_address2': 'Street Address 2',
            'billing_town_or_city': 'Town or City',
            'billing_postcode': 'Postal Code',
            'billing_county': 'County, State or Locality',
        }

        no_placeholders = ['delivery_country', 'billing_country',
                           'billing_same_as_delivery', 'gift_option'
                           ]

        for field in self.fields:
            if field not in no_placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields['gift_option'].label = "Add gift option"
        self.fields['billing_same_as_delivery'].label = (
            'My billing address is the same as my delivery address')
