"""
URL patterns for Bag application
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.view_bag, name="bag"),
    path("add/<int:artwork_id>/", views.add_to_bag, name="add_to_bag"),
    path("adjust/<artwork_id>/", views.adjust_bag, name="adjust_bag"),
    path("remove/<artwork_id>/", views.remove_from_bag,
         name="remove_from_bag"),
    path("gift_option/", views.gift_option, name="gift_option"),
]
