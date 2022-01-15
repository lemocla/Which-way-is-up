"""
Models configuration for Portfolio application
"""

from django.db import models
from django.db import transaction
from .fields import CaseInsensitiveCharField


class PortfolioCategory(models.Model):
    """
    Stores portfolio categories details
    """
    class Meta:
        """Order by name"""
        ordering = ['name']
        verbose_name_plural = "Portfolio categories"

    name = CaseInsensitiveCharField(max_length=150, unique=True)

    def __str__(self):
        return str(self.name)


class Portfolio(models.Model):
    """
    Stores portfolio details
    Related to PortfolioCategory model
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
    description = models.TextField(max_length=1500)
    materials = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey('PortfolioCategory',
                                 null=True,
                                 blank=False,
                                 on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    homepage = models.BooleanField(default=False)

    def __str__(self):
        """return name as string"""
        return str(self.name)

    # https://stackoverflow.com/questions/1455126/unique-booleanfield-value-in-django
    def save(self, *args, **kwargs):
        """
        Override save model so that one boolean is selected to display on
        homepage
        """
        if not self.homepage:
            return super(Portfolio, self).save(*args, **kwargs)
        with transaction.atomic():
            Portfolio.objects.filter(
                homepage=True).update(homepage=False)
            return super(Portfolio, self).save(*args, **kwargs)
