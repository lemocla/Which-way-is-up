"""
URL pattern for about page
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.profile, name="profile"),
    path('wishlist/', views.wishlist, name='wishlist'),
    path("add_to_wishlist/<artwork_id>", views.add_to_wishlist,
          name="add_to_wishlist"),
]
