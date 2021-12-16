"""
URL patterns for policies
"""
from django.urls import path
from . import views


urlpatterns = [
    path("delivery_and_returns", views.delivery_returns,
         name="delivery_and_returns"),
]
