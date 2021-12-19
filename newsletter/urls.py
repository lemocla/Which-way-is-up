"""
URL patterns for newsletter mailing list
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_to_mailing_list, name='newsletter'),
]
