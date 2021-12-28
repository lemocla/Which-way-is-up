"""
URL pattern for bag app
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.bag, name="bag"),
    path("add/<int:artwork_id>/", views.add_to_bag, name="add_to_bag"),
]
