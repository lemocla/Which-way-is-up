"""
Admin configuration for Artwork app
"""
from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ShopCategory, Artwork


class ShopCategoryAdmin(admin.ModelAdmin):
    """
    Admin setting to display list of shop category,
    Ordered by date created at
    """
    model = ShopCategory
    list_display = (
        "name",
        "backend_name"
    )
    ordering = ('created_at',)


class ArtworkAdmin(admin.ModelAdmin):
    """
    Admin setting to display list of artwork,
    Ordered by name, with a vertical filter and a
    Search box
    Widget to display image thumbnail in list display
    """

    model = Artwork
    # https://stackoverflow.com/questions/2443752/django-display-image-in-admin-interface

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
    search_fields = ['name', 'status', 'shop_category__name',
                     'portfolio__name']

    actions = ['delete_selected']

    def admin_image(self, model):
        """
        Render image in artwork list display
        """
        if model.image:
            img_path = settings.MEDIA_URL
            return mark_safe(
                f'<img src="{img_path}%s" width="50" height="50"'
                f' alt="product image"/>' % model.image)

    admin_image.allow_tags = True

    def delete_queryset(self, request, queryset):
        """Override delete queryset to call delete method"""
        for obj in queryset:
            obj.post_delete()

    @admin.action(description='Mark as draft')
    def make_draft(self, request, queryset):
        """Update selected artworks' status as draft"""
        queryset.update(status='draft')

    @admin.action(description='Mark as active')
    def make_active(self, request, queryset):
        """Update selected artworks' status as active"""
        queryset.update(status='active')

    @admin.action(description='Mark as inactive')
    def make_inactive(self, request, queryset):
        """Update selected artworks' status as inactive"""
        queryset.update(status='inactive')
        # Call save method for object in queryset
        for obj in queryset:
            obj.save()

    actions = [make_draft, make_active, make_inactive]


admin.site.register(ShopCategory, ShopCategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)
