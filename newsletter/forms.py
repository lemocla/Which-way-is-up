"""
form to add email to mailing list
"""

from django import forms
from .models import Mailing
# https://docs.djangoproject.com/en/4.0/topics/forms/


class SubscribeForm(forms.ModelForm):
    """
    Set fields for newsletter subscription form
    based on Mailing model
    """
    class Meta:
        model = Mailing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] =  "name@example.com"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].error_messages["required"] = "Please enter a valid email address"



 