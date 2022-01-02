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
        "ratings",
        "comments",
        "user_profile",
        "artwork",
        "created_at"
    )


admin.site.register(Review, ReviewAdmin)
