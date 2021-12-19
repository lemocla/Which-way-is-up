"""
form for newsletter subscription
"""

from django import forms
from .models import Subscription
# https://docs.djangoproject.com/en/4.0/topics/forms/


class SubscribeForm(forms.ModelForm):
    """
    form fields for newsletter subscription
    based on Subscription model
    """
    class Meta:
        model = Subscription
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



 