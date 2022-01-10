"""
Admin configuration for reviews application
"""

from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin settings to display list of Reviews
    Ordered by date created and ratings
    Vertical filter by ratings
    """

    model = Review
    list_display = (
        'artwork',
        'created_at',
        'ratings',
        'user_profile',
    )

    ordering = ('-created_at', '-ratings', )
    list_filter = ('ratings',)


admin.site.register(Review, ReviewAdmin)
