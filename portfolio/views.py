"""
Views to handle display and portfolio management
"""
from django.shortcuts import render, get_object_or_404

from .models import Portfolio


def portfolio_detail(request, portfolio_id):
    """
    View portfolio detail
    """
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio.html', context)
