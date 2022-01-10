"""
Forms configuration for Contact application
"""

from django import forms
# https://docs.djangoproject.com/en/4.0/topics/forms/


class ContactForm(forms.Form):
    """
    Form to collect contact form details
    """
    full_name = forms.CharField(
        label='Full name',
        required=True,
        min_length=1, max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your name'}),
        error_messages={'required': 'Please enter your name'}
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Your email address'}),
        error_messages={'required': 'Please enter a valid email address'}
    )

    subject = forms.CharField(
        label='Subject',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
        max_length=100
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '6',
                                     'placeholder': 'Your message'}),
        required=True, min_length=3,
        max_length=1500,
        error_messages={'required': 'Please enter a message in the text area'}
    )
