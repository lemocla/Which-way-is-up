"""
Models to manage artwork and shop categories
"""

from django.db import models, transaction
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
    backend_name = CaseInsensitiveCharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        with transaction.atomic():
            str_name = self.name
            self.backend_name = str_name.replace(' ', '_')
            return super(ShopCategory, self).save(*args, **kwargs)
