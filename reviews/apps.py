"""
Configuration for Reviews application
"""

from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Configure reviews application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'

    def ready(self):
        """Import review signals"""
        import reviews.signals
