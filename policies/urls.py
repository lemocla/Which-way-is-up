"""
URL patterns for policies application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("delivery_and_returns", views.delivery_returns,
         name="delivery_and_returns"),
    path("terms_and_conditions", views.terms_conditions,
         name="terms_and_conditions"),
    path("accessibility", views.accessibility, name="accessibility"),
    path("privacy", views.privacy, name="privacy"),
]
