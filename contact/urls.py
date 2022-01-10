"""
URL patterns for Contact application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.contact, name="contact"),
]
