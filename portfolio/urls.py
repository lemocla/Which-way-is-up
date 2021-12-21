"""
Urls for portfolio app
"""

from django.urls import path
from . import views


urlpatterns = [
    path('<int:portfolio_id>/', views.portfolio_detail,
         name='portfolio_detail'),
]
