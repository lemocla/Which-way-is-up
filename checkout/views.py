"""
Views to handle checkout functionalities
"""
from django.shortcuts import render
from .forms import OrderForm


def checkout(request):
    """
    Views to display checkout page
    """
    form = OrderForm()
    context = {
        "form": form,
    }
    return render(request, 'checkout/checkout.html', context)
