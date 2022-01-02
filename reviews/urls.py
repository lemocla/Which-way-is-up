"""
URL patterns for reviews app
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_reviews, name="reviews"),
    path("add_reviews/<int:artwork_id>/<int:orderline_id>/",
         views.add_reviews, name="add_reviews"),
]
