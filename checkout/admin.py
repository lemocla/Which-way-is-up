"""
Admin models for artwork app
"""

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Admin model to display line of items for each order
    """
    model = OrderLineItem
    # https://stackoverflow.com/questions/37338925/django-tabularinline-discard-empty-rows
    extra = 0
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin model to display order information
    """

    model = Order
    inlines = (OrderLineItemAdminInline,)
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
