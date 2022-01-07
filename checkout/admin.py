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

    @admin.action(description='Mark as dispatched')
    def dispatched(modeladmin, request, queryset):
        queryset.update(status='dispatched')

    list_display = (
        'order_number',
        'date',
        'full_name',
        'gift_option',
        'total',
        'paid',
        'status',
    )
    actions = [dispatched]
    ordering = ('-date',)
    list_filter = ('status', 'paid')
    search_fields = ['full_name', 'date', 'order_number', 'lineitems__artwork__name']




admin.site.register(Order, OrderAdmin)
