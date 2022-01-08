"""
URL pattern for about page
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.about, name="about"),
    path("add_event", views.add_event, name="add_event"),
]
