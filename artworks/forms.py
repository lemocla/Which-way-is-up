"""
Forms configuration for Artwork application
"""

from django import forms
from portfolio.widgets import CustomClearableFileInput
from .models import Artwork


class ArtworkForm(forms.ModelForm):
    """
    Configure model form to add/edit an artwork
    """
    class Meta:
        """Set fields from artwork model"""
        model = Artwork
        exclude = ('rating',)

    # Custom image form widgget
    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Set placeholders and labels for fields in the form
        """
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
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholders[field]

        self.fields['size'].label = 'Size (in cm)'
        self.fields['shop_category'].label = 'Select shop category'
        self.fields['portfolio'].label = 'Select portfolio category'
        self.fields['related_items'].label = 'Select one or more related items'
        self.fields['display_shop'].label = 'Display on shop'
        self.fields['related_items'].widget.attrs['class'] = 'select-height'
