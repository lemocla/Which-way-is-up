"""
Form definition for add and edit an event
"""
from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    Model form to add/edit an portfolio
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
            format=('%d-%m-%Y'),
            attrs={'placeholder': 'Enter date ex. 10/01/2021',
                   'type': 'date'}))
    date_end = forms.DateField(
        required=False,
        widget=forms.DateInput(
            format=('%d-%m-%Y'),
            attrs={'placeholder': 'Enter date ex. 10/01/2021',
                   'type': 'date'}))

    place = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter event name & location'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
