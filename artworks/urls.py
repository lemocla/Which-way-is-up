"""
URL patterns for Artwork application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.artworks, name="shop"),
    path('<int:artwork_id>/', views.artwork_detail, name='artwork_details'),
    path('add/', views.add_artwork, name='add_artwork'),
    path('edit/<int:artwork_id>/', views.edit_artwork, name='edit_artwork'),
    path('delete/<int:artwork_id>/', views.delete_artwork,
         name='delete_artwork'),
]
