"""
Admin models for portfolio app
"""

from django.contrib import admin
from django.utils.safestring import mark_safe
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
    model = Portfolio

    def admin_image(self, model):
        """
        Render image in admin panel
        """
        if model.image:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" alt="product image"/>' % model.image)

    list_display = (
        'name',
        'category',
        'status',
        'admin_image',
    )

    list_filter = ('status', 'category')

    ordering = ('category', 'name',)
    search_fields = ['name', 'status', 'category__name']

    @admin.action(description='Mark as draft')
    def make_draft(modeladmin, request, queryset):
        queryset.update(status='draft')

    @admin.action(description='Mark as active')
    def make_active(modeladmin, request, queryset):
        queryset.update(status='active')

    @admin.action(description='Mark as inactive')
    def make_inactive(modeladmin, request, queryset):
        queryset.update(status='inactive')

    actions = [make_draft, make_active, make_inactive]

admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
