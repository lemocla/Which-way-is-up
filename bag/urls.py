"""
URL pattern for bag app
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.bag, name="bag"),
]
