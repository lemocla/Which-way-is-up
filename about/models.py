"""
Models configuration for About application
"""
from datetime import datetime
from django.db import models


class Event(models.Model):
    """
    Store event details with date format YYYY-MM-DD
    """
    class Meta:
        """Order by most recent date"""
        ordering = ['-date_start']

    date_start = models.DateField(auto_now=False, auto_now_add=False,
                                  null=False, blank=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False, null=True,
                                blank=True)
    place = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.date_start} - {self.place}'

    def save(self, *args, **kwargs):
        """Override save method to ensure valid date format"""
        self.date_start = datetime.strftime(self.date_start, '%Y-%m-%d')
        if self.date_end:
            self.date_end = datetime.strftime(self.date_end, '%Y-%m-%d')
        return super(Event, self).save(*args, **kwargs)
