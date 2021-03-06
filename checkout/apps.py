"""
Checkout application configuration
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configure Checkout application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """Import signals"""
        import checkout.signals
