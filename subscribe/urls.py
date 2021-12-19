"""
URL patterns for newsletter subscription
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_to_subscribe_list, name='subscribe'),
]
