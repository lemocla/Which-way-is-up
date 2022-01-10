"""
Artwork application configuration
"""
from django.apps import AppConfig


class ArtworksConfig(AppConfig):
    """
    Configure Artwork application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artworks'
