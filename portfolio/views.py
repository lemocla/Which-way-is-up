"""
Views to handle display and portfolio management
"""
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from artworks.models import Artwork
from .forms import PortfolioForm
from .models import Portfolio


def portfolio_detail(request, portfolio_id):
    """
    View portfolio detail
    """
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    artworks = Artwork.objects.filter(portfolio=portfolio).values()
    context = {
        'portfolio': portfolio,
        'artworks': artworks
    }

    return render(request, 'portfolio/portfolio.html', context)


@login_required
def add_portfolio(request):
    """
    Add portfolio to database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect(reverse('home'))

    if request.method == 'POST':

        form = PortfolioForm(request.POST, request.FILES)

        if form.is_valid():
            # Data from form
            portfolio = form.save()
            messages.success(request, 'Portfolio successfully added!')
            return redirect(reverse('portfolio_detail', args=[portfolio.id]))
        else:
            messages.error(request, 'Portfolio couldn\'t be added. '
                           'Please ensure the form is valid.')
    else:
        form = PortfolioForm()

    context = {
        'form': form,
    }

    return render(request, "portfolio/add_portfolio.html", context)


@login_required
def edit_portfolio(request, portfolio_id):
    """
    Edit portfolio in the database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect(reverse('home'))

    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    if request.method == 'POST':

        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)

        if form.is_valid():
            # Data from form
            form.save()
            messages.success(request, 'Portfolio successfully updated!')
            return redirect(reverse('portfolio_detail', args=[portfolio.id]))
        else:
            messages.error(request, 'Portfolio couldn\'t be updated. '
                           'Please ensure the form is valid.')
    else:
        form = PortfolioForm(instance=portfolio)
        messages.info(request, f'Editing {portfolio.name}')

    context = {
        'form': form,
        'portfolio': portfolio
    }

    return render(request, "portfolio/edit_portfolio.html", context)


@login_required
def delete_portfolio(request, portfolio_id):
    """
    Delete portfolio from the database
    """
    # Additional security to restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to shop owner')
        return redirect(reverse('home'))

    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    portfolio.delete()
    messages.success(request, 'Portfolio successfully deleted!')
    return redirect(reverse('home'))
