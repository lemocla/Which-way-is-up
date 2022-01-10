"""
URL patterns for newsletter application
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_to_mailing_list, name='newsletter'),
]
