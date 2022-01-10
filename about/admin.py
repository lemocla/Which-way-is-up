"""
Admin configuration for About app
"""

from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Event admin settings to display list of events,
    Ordered by most recent date, with a vertical filter and a
    Search box
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
