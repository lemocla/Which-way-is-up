"""
Admin models for portfolio app
"""

from django.contrib import admin
from .models import PortfolioCategory


class PortfolioCategoryAdmin(admin.ModelAdmin):
    """
    Admin model to display user portfolio categories
    Display category name
    """
    model = PortfolioCategory
    list_display = (
        "name",
    )


admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
