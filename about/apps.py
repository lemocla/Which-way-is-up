"""
About application configuration
"""

from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configure About application module
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
