"""
Admin configuration for portfolio application
"""
from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import PortfolioCategory, Portfolio


class PortfolioCategoryAdmin(admin.ModelAdmin):
    """
    Admin setting to display user portfolio categories
    Display category name
    """
    model = PortfolioCategory
    list_display = (
        "name",
    )


class PortfolioAdmin(admin.ModelAdmin):
    """
    Admin setting to display list of portfolios with
    - widget to display image cover
    - vertical filter
    - search box
    - custom actions to set portfolio as active, inactive, draft
    """
    model = Portfolio

    def admin_image(self, model):
        """
        Render image in admin panel
        """
        if model.image:
            img_path = settings.MEDIA_URL
            return mark_safe(
                f'<img src="{img_path}%s" width="50" height="50" '
                f'alt="product image"/>' % model.image)

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
    def make_draft(self, request, queryset):
        """Set queryset as draft"""
        queryset.update(status='draft')

    @admin.action(description='Mark as active')
    def make_active(self, request, queryset):
        """Set queryset as active"""
        queryset.update(status='active')

    @admin.action(description='Mark as inactive')
    def make_inactive(self, request, queryset):
        """Set queryset as inactive"""
        queryset.update(status='inactive')

    actions = [make_draft, make_active, make_inactive]


admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
