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
