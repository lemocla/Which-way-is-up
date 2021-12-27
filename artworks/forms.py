"""
Form definition for artwork app
"""
from django import forms
from django.db import models
from portfolio.widgets import CustomClearableFileInput
from portfolio.models import Portfolio, PortfolioCategory
from .models import ShopCategory, Artwork


class ArtworkForm(forms.ModelForm):
    """
    Model form to add a artwork
    """
    class Meta:
        """All fields from porfolio model """
        model = Artwork
        # fields = '__all__'
        exclude = ('rating',)

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter artwork name',
            'size': 'Ex. 40 x 40',
            'materials': 'Ex. pen on card',
            'year': 'Ex. 2020',
            'price': 'Ex. 100 or 30.50',
            'sale_price': 'Ex. 100 or 30.50',
        }
        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]

        self.fields['size'].label = 'Size (in cm)'
        self.fields['shop_category'].label = 'Select shop category'
        self.fields['portfolio'].label = 'Select portfolio category'
        self.fields['related_items'].label = 'Select one or more related items'
        self.fields['display_shop'].label = 'Display on shop'
