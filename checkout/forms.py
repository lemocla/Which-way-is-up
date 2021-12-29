"""
Forms for oder model
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form field for personal information
    """
    class Meta:
        model = Order
        exclude = ('order_number', 'date', 'bag',
                   'user_profile', 'total', 'status')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'gift_option': 'This order is a gift',
            'gift_recipient': 'Enter gift recipient',
            'gift_message': 'Personalise your message',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        no_placeholders = ['country']
        for field in self.fields:
            if field not in no_placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mb-3'
