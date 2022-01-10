"""
Forms configuration for Review application
"""

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Model form to add/edit a review
    """
    class Meta:
        """Set up form for review model """
        model = Review
        exclude = ('user_profile', 'order_line', 'artwork', 'created_at')

    comments = forms.CharField(
        widget=forms.Textarea(attrs={
                              'rows': '4',
                              'placeholder': 'Add a comment'})
    )

    def __init__(self, *args, **kwargs):
        """initialise form"""
        super().__init__(*args, **kwargs)
