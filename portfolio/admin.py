"""
Admin models for portfolio app
"""

from django.contrib import admin
from .models import PortfolioCategory, Portfolio


class PortfolioCategoryAdmin(admin.ModelAdmin):
    """
    Admin model to display user portfolio categories
    Display category name
    """
    model = PortfolioCategory
    list_display = (
        "name",
    )


class PortfolioAdmin(admin.ModelAdmin):
    """
    Admin panel for portfolios
    """
    list_display = (
        'name',
        'category',
        'status',
    )
    ordering = ('category', 'name',)


admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
