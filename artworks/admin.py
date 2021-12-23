"""
Admin models for portfolio app
"""

from django.contrib import admin
from .models import ShopCategory


class ShopCategoryAdmin(admin.ModelAdmin):
    """
    Admin model to display user portfolio categories
    Display category name
    """
    model = ShopCategory
    list_display = (
        "name",
    )
    ordering = ('created_at',)


admin.site.register(ShopCategory, ShopCategoryAdmin)
