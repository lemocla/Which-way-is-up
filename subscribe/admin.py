from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    """
    Admin model to display subscription
    Display field email
    """
    model = Subscription
    list_display = (
        "email",
    )

admin.site.register(Subscription, SubscriptionAdmin)