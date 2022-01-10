"""
Newsletter application configuration
"""

from django.apps import AppConfig


class SubscribeConfig(AppConfig):
    """
    Configure newletter application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'
