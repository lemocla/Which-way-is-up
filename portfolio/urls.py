"""
Urls patterns for portfolio app
"""

from django.urls import path
from . import views


urlpatterns = [
    path('<int:portfolio_id>/', views.portfolio_detail,
         name='portfolio_detail'),
    path('add/', views.add_portfolio, name='add_portfolio'),
    path('edit/<int:portfolio_id>/', views.edit_portfolio,
         name='edit_portfolio'),
    path('delete/<int:portfolio_id>/', views.delete_portfolio,
         name='delete_portfolio'),
]
