from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    """
    Admin model to display user profile
    Display user name
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


admin.site.register(UserProfile, ProfileAdmin)
