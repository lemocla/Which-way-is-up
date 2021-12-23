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
        return mark_safe(
            '<img src="/media/%s" width="50" height="50"/>' % model.image)
    admin_image.allow_tags = True

    list_display = (
        "admin_image",
        "name",
        "size",
        "price",
        "stock",
        "portfolio",
        "shop_category",
        "status"
    )
    ordering = ('name',)


admin.site.register(ShopCategory, ShopCategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)
