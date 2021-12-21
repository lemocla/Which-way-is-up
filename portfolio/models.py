"""
Models to manage portfolio and portfolios categories
"""

from django.db import models


class PortfolioCategory(models.Model):
    """
    Model for portfolio categories
    """
    class Meta:
        """Order by name"""
        ordering = ['name']
        verbose_name_plural = "Portfolio categories"

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
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

    name = models.CharField(max_length=150)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=1500)
    materials = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey('PortfolioCategory',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.name
