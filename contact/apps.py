"""
Contact application configuration
"""
from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    Configure Contact application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
