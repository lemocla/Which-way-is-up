"""
Admin configuration for Profiles application
"""

from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    """
    Admin setting to display of profiles with
    Search box
    """
    model = UserProfile
    list_display = (
        "user",
        "full_name",
        "street_address1",
        "town_or_city",
        "postcode",
        "newsletter"
    )
    search_fields = ['full_name', 'user__email']


admin.site.register(UserProfile, ProfileAdmin)
