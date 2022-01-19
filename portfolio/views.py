"""
Views to manage artworks CRUD operations
"""

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from artworks.models import Artwork
from profiles.models import UserProfile
from .forms import PortfolioForm
from .models import Portfolio


def portfolio_detail(request, portfolio_id):
    """
    View to display portfolio detail
    Get wishlist if user authenticated
    Restrict access to super user for non active items
    """
    user = None
    wishlist = None

    # Get wishlist items if user authenticated
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = user.wishlist_items.values()

    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    # restrict access to draft/inactive porfolio
    if portfolio.status != 'active':
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, access restricted to the shop '
                           'owner')
            return redirect(reverse('home'))

    # Get artworks
    artworks = Artwork.objects.filter(portfolio=portfolio).filter(
                status='active').values()

    # Set context
    context = {
        'portfolio': portfolio,
        'artworks': artworks,
        'user': user,
        "wishlist": wishlist
    }

    return render(request, 'portfolio/portfolio.html', context)


@login_required
def add_portfolio(request):
    """
    View to add portfolio to database
    Display the add to portfolio page
    Restrict access to super user
    """

    # Restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to the shop owner')
        return redirect(reverse('home'))

    if request.method == 'POST':

        # Instanciate form with post data and files
        form = PortfolioForm(request.POST, request.FILES)

        if form.is_valid():
            # Save data from form
            portfolio = form.save()
            # Success message
            messages.success(request, 'Portfolio successfully added!')
            return redirect(reverse('portfolio_detail', args=[portfolio.id]))
        else:
            # Error message
            messages.error(request, 'Portfolio couldn\'t be added. '
                           'Please ensure the form is valid.')
    else:
        # Instanciate empty form
        form = PortfolioForm()

    # Set context
    context = {
        'form': form,
    }

    return render(request, "portfolio/add_portfolio.html", context)


@login_required
def edit_portfolio(request, portfolio_id):
    """
    View to edit portfolio in the database
    Display edit porfolio page
    Restrict access to superuser
    """

    # Restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to the shop owner')
        return redirect(reverse('home'))

    # Get portfolio object
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    if request.method == 'POST':
        # Instanciate form with portfolio post data and files
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)

        if form.is_valid():
            # Save data from form
            form.save()
            # Success message
            messages.success(request, 'Portfolio successfully updated!')
            return redirect(reverse('portfolio_detail', args=[portfolio.id]))
        else:
            # Error message
            messages.error(request, 'Portfolio couldn\'t be updated. '
                           'Please ensure the form is valid.')
    else:
        # Instanciate form with portfolio data
        form = PortfolioForm(instance=portfolio)
        # Information message
        messages.info(request, f'Editing {portfolio.name}')

    # Set context
    context = {
        'form': form,
        'portfolio': portfolio
    }

    return render(request, "portfolio/edit_portfolio.html", context)


@login_required
def delete_portfolio(request, portfolio_id):
    """
    View to delete portfolio from the database
    """
    # Restrict access to shop owner
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access restricted to the shop owner')
        return redirect(reverse('home'))

    # Get portfolio object
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)

    # Delete portfolio
    portfolio.delete()

    # Success message
    messages.success(request, 'Portfolio successfully deleted!')
    return redirect(reverse('home'))
