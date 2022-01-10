"""
Forms configuration for profile model
"""

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, ButtonHolder, Submit

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to collect users' personal information
    """
    class Meta:
        """Configure model and fields"""
        model = UserProfile
        exclude = ('user', 'wishlist_items')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        Use Crispy helper to design layout and style
        """

        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'profile'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    HTML("<h2 class='trapez-bg fs-4 ps-4 py-1 mb-4 mb-md-5'>"
                         "Your contact details</h2>"),
                    'full_name',
                    'phone_number',
                    'newsletter',
                    css_class="col-12 col-lg-6 pe-lg-5",
                ),
                Div(
                    HTML("<h2 class='trapez-bg fs-4 ps-4 py-1 mb-4 mb-md-5'>"
                         "Default address</h2>"),
                    'street_address1',
                    'street_address2',
                    'postcode',
                    'county',
                    'town_or_city',
                    'country',
                    css_class="col-12 col-lg-6 ps-lg-5",
                ),
                ButtonHolder(
                    Submit(
                         'update',
                         'Update',
                         css_class="btn border-dark btn-black px-5 py-2 "
                         "text-uppercase"),
                    HTML("<a class='btn btn-white px-5 py-2 text-uppercase' "
                         "href='{% url \"profile\" %}'>Cancel</a>"),
                    css_class="mt-4 text-center"
                ), css_class="row", css_id="profile-form"
            )
        )

        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        no_placeholders = ['country', 'newsletter']
        for field in self.fields:
            if field not in no_placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mb-3'
