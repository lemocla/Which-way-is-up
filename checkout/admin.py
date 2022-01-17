"""
Admin configuration for Checkout application
"""

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Admin setting to display line of items for each order
    """
    model = OrderLineItem
    # https://stackoverflow.com/questions/37338925/django-tabularinline-discard-empty-rows
    extra = 0
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin setting to display order information with
    - inline display for Order Line
    - filter by status, paid and full name
    - search box
    - custom action to mark order as dispatched
    """

    model = Order
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'total',
                       'bag',)

    list_display = (
        'order_number',
        'date',
        'full_name',
        'gift_option',
        'total',
        'paid',
        'status',
    )

    ordering = ('-date',)
    list_filter = ('status', 'paid', 'full_name', 'lineitems__artwork__name')
    search_fields = ['full_name', 'date', 'order_number',
                     'lineitems__artwork__name']

    @admin.action(description='Mark as dispatched')
    def dispatched(self, request, queryset):
        """
        Custom action to mark order as dispatched
        """
        queryset.update(status='dispatched')

    actions = [dispatched]


admin.site.register(Order, OrderAdmin)
