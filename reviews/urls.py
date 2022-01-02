"""
URL patterns for reviews app
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_reviews, name="reviews"),
    path("add_reviews/<int:artwork_id>/<int:orderline_id>/",
         views.add_reviews, name="add_reviews"),
    path('edit_reviews/<int:review_id>/', views.edit_reviews,
         name='edit_reviews'),
    path('delete_reviews/<int:review_id>/', views.delete_reviews,
         name='delete_reviews'),
]
