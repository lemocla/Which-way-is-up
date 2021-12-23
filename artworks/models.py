"""
Models to manage artwork and shop categories
"""

from django.db import models
from portfolio.fields import CaseInsensitiveCharField


class ShopCategory(models.Model):
    """
    Model for shop categories
    """
    class Meta:
        """Order by name"""
        ordering = ['created_at']
        verbose_name_plural = "Shop categories"

    name = CaseInsensitiveCharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
