"""
Forms configuration for About application
"""
from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    Configure model form to add/edit an event
    """
    class Meta:
        """All fields from event model """
        model = Event
        fields = '__all__'

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
                              'rows': '3',
                              'placeholder': 'Enter event desciption'}))

    # https://stackoverflow.com/questions/61076688/django-form-dateinput-with-widget-in-update-loosing-the-initial-value
    date_start = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}))

    date_end = forms.DateField(
        required=False,
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}))

    place = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter event name & location'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
