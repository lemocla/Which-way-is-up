"""
Form definition for portfolio application
"""

from django import forms
from .widgets import CustomClearableFileInput
from .models import PortfolioCategory, Portfolio


class PortfolioForm(forms.ModelForm):
    """
    Configure model form to add/edit a portfolio
    """
    class Meta:
        """All fields from porfolio model """
        model = Portfolio
        fields = '__all__'

    description = forms.CharField(
        widget=forms.Textarea(attrs={
                              'rows': '7',
                              'placeholder': 'Enter description'})
    )
    materials = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
                              'rows': '3',
                              'placeholder': 'Enter materials and mediums'})
    )

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = PortfolioCategory.objects.all()
        self.fields['category'].choices = categories.values_list()
        self.fields['homepage'].label = 'Display on homepage'
