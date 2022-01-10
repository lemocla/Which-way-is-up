"""
Form to add email to mailing list
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
        """
        Newsletter form configuration
        """
        model = Mailing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        self.fields["email_newsletter"].widget.attrs[
         "placeholder"] = "name@example.com"
        self.fields["email_newsletter"].widget.attrs[
         "class"] = "form-control"
        self.fields["email_newsletter"].error_messages[
         "required"] = "Please enter a valid email address"
