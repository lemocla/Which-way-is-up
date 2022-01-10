"""
Portfolio application configuration
"""

from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """
    Configure portfolio application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
