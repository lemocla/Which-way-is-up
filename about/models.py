"""
Models for about app
"""

from django.db import models


class Event(models.Model):
    """
    Model to store event details
    """
    class Meta:
        """Order by name"""
        ordering = ['-date_start']

    date_start = models.DateField(auto_now=False, auto_now_add=False,
                                  null=False, blank=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False, null=True,
                                blank=True)
    place = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.date_start} - {self.place}'
