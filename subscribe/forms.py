"""
form for newsletter subscription
"""

from django import forms

# https://docs.djangoproject.com/en/4.0/topics/forms/


class SubscribeForm(forms.Form):
    """
    form fields for newsletter subscription
    """

    email = forms.EmailField(
        label='Email',
        required=False,
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}),
        error_messages={'required': 'Please enter a valid email address'}
    )

    email.widget.attrs.update({'class': 'form-control'})
