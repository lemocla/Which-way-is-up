"""
URL pattern for about page
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.artworks, name="shop"),
]
