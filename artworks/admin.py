"""
Admin models for artwork app
"""

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ShopCategory, Artwork


class ShopCategoryAdmin(admin.ModelAdmin):
    """
    Admin model to display user portfolio categories
    Display category name
    """
    model = ShopCategory
    list_display = (
        "name",
        "backend_name"
    )
    ordering = ('created_at',)


class ArtworkAdmin(admin.ModelAdmin):
    """
    Admin model to display user portfolio categories
    Display category name
    """

    model = Artwork
    # https://stackoverflow.com/questions/2443752/django-display-image-in-admin-interface

    def admin_image(self, model):
        """
        Render image in admin panel
        """
        if model.image:
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" alt="product image"/>' % model.image)

    admin_image.allow_tags = True

    list_display = (
        'name',
        'size',
        'price',
        'stock',
        'portfolio',
        'shop_category',
        'display_shop',
        'status',
        'admin_image',
    )
    list_filter = ('status', 'portfolio', 'shop_category', 'stock')
    ordering = ('name',)
    search_fields = ['name', 'status', 'shop_category__name', 'portfolio__name']

    actions = ['delete_selected']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

    @admin.action(description='Mark as draft')
    def make_draft(self, request, queryset):
        queryset.update(status='draft')

    @admin.action(description='Mark as active')
    def make_active(self, request, queryset):
        queryset.update(status='active')

    @admin.action(description='Mark as inactive')
    def make_inactive(self, request, queryset):
        queryset.update(status='inactive')
        for obj in queryset:
            obj.save()

    actions = [make_draft, make_active, make_inactive]


admin.site.register(ShopCategory, ShopCategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)
