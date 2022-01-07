"""
Admin models for reviews app
"""

from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin model to display reviews
    """
    model = Review
    list_display = (
        "artwork",
        "created_at",
        "ratings",
        "comments",
        "user_profile",
    )
    ordering = ('-created_at', '-ratings', )


admin.site.register(Review, ReviewAdmin)
