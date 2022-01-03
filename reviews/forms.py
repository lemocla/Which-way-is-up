"""
Form definition for portfolio app
"""
from django import forms
from .models import Review


class PortfolioForm(forms.ModelForm):
    """
    Model form to add a portfolio
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
        super().__init__(*args, **kwargs)
