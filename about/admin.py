from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Admin model to display user portfolio categories
    Display category name
    """

    model = Event

    list_display = (
        'date_start',
        'date_end',
        'place',
        'description',
    )
    list_filter = ('date_start',)
    ordering = ('-date_start',)
    search_fields = ['place', 'date_start', 'description']


admin.site.register(Event, EventAdmin)
