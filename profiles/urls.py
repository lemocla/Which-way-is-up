"""
URL patterns for Profile application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.profile, name="profile"),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path("add_to_wishlist/<artwork_id>", views.add_to_wishlist,
         name="add_to_wishlist"),
    path("remove_from_wishlist/<artwork_id>", views.remove_from_wishlist,
         name="remove_from_wishlist"),
    path('order_history', views.order_history, name='order_history'),
    path('my_reviews', views.my_reviews, name='my_reviews'),
    path('order_details/<order_number>', views.order_details,
         name='order_details'),
]
