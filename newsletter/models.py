"""
Models for newsletter mailing list
"""

from django.db import models


class Mailing(models.Model):
    """
    Model to store email address for database
    """
    email_newsletter = models.EmailField(max_length=255, null=False,
                                         blank=False, unique=True)

    class Meta:
        """
        Add verbose name
        """
        verbose_name = 'Mailing List'

    def __str__(self):
        return str(self.email_newsletter)
