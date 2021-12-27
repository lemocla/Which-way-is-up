"""
URL pattern for about page
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.artworks, name="shop"),
    path('<int:artwork_id>/', views.artwork_detail,
         name='artwork_details'),
    path('add/', views.add_artwork, name='add_artwork'),
]
