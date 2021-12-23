"""
Models to manage artwork and shop categories
"""

from django.db import models, transaction
from django.core.validators import MaxValueValidator, MinValueValidator
from portfolio.fields import CaseInsensitiveCharField
from portfolio.models import Portfolio


class ShopCategory(models.Model):
    """
    Model for shop categories
    """
    class Meta:
        """Order by name"""
        ordering = ['created_at']
        verbose_name_plural = "Shop categories"

    name = CaseInsensitiveCharField(max_length=150, unique=True)
    backend_name = CaseInsensitiveCharField(max_length=150,
                                            null=True,
                                            blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        with transaction.atomic():
            str_name = self.name
            self.backend_name = str_name.replace(' ', '_')
            return super(ShopCategory, self).save(*args, **kwargs)


class Artwork(models.Model):
    """
    Model for portfolio
    """
    class Meta:
        """Order by name"""
        ordering = ['name']

    ACTIVE = 'active'
    DRAFT = 'draft'
    INACTIVE = 'inactive'

    STATUS = [
        (ACTIVE, 'active'),
        (DRAFT, 'draft'),
        (INACTIVE, 'inactive'),
    ]

    name = CaseInsensitiveCharField(max_length=150, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    materials = models.CharField(max_length=500)
    size = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator('0.00')])
    # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    stock = models.PositiveSmallIntegerField(default=1,
                                             validators=[
                                                MaxValueValidator(500),
                                                MinValueValidator(1)
                                             ])
    portfolio = models.ForeignKey(Portfolio,
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL)
    shop_category = models.ForeignKey('ShopCategory',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL)
    related_items = models.ForeignKey("self", null=True,
                                      blank=True, on_delete=models.SET_NULL)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6,
                                     decimal_places=2,
                                     null=True,
                                     blank=True,
                                     validators=[
                                        MinValueValidator('0.00')
                                     ])
    rating = models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default=ACTIVE)
    display_shop = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
