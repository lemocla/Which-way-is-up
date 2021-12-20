"""
Forms for profile model
"""
from django import forms
from .models import UserProfile


class DeliveryForm(forms.ModelForm):
    """
    Form fields for default delivery details
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'full_name', 'phone_number', 'newsletter')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class ContactDetailsForm(forms.ModelForm):
    """
    Form field for personal information
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'street_address1', 'street_address2', 'postcode',
                   'county', 'town_or_city', 'country')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'newsletter': 'Subscribe to newsletter'
        }

        for field in self.fields:
            self.fields[field].widget.attrs[
             'placeholder'] = placeholders[field]
