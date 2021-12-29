"""
Admin models for artwork app
"""

from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """
    Admin model to display order information
    """

    model = Order
    
    readonly_fields = ('order_number', 'date', 'total',
                       'bag',)

    list_display = (
        "order_number",
        "date",
        "full_name",
        "gift_option",
        "total",
        "status",
    )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
