"""
Models configuration for Checkout App
"""

import uuid

from django.db import models
from django.db.models import Sum
from django_countries import Countries
from django_countries.fields import CountryField
from profiles.models import UserProfile
from artworks.models import Artwork


class Order(models.Model):
    """
    Stores order details and related to UserProfile model
    """
    class Meta:
        """Order by date"""
        ordering = ['date']

    IN_PROGRESS = 'in progress'
    DISPATCHED = 'dispatched'

    STATUS = [
        (IN_PROGRESS, 'in progress'),
        (DISPATCHED, 'dispatched'),
    ]

    # https://pypi.org/project/django-countries/#customize-the-country-list
    class G8Countries(Countries):
        """ Restrict delivery countries to GB only """
        only = ['GB']

    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    # user personal details
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    # delivery address
    delivery_street_address1 = models.CharField(max_length=80, null=False,
                                                blank=False)
    delivery_street_address2 = models.CharField(max_length=80, null=True,
                                                blank=True)
    delivery_town_or_city = models.CharField(max_length=40, null=False,
                                             blank=False)
    delivery_county = models.CharField(max_length=80, null=True, blank=True)
    delivery_country = CountryField(blank_label='Country *', null=False,
                                    max_length=80, blank=False,
                                    countries=G8Countries)
    delivery_postcode = models.CharField(max_length=20, null=False,
                                         blank=False)
    # billing address
    billing_same_as_delivery = models.BooleanField(default=True)
    billing_street_address1 = models.CharField(max_length=80, null=False,
                                               blank=False)
    billing_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    billing_town_or_city = models.CharField(max_length=40, null=False,
                                            blank=False)
    billing_county = models.CharField(max_length=80, null=True, blank=True)
    billing_country = CountryField(blank_label='Country *', null=False,
                                   blank=False, max_length=80)
    billing_postcode = models.CharField(max_length=20, null=True, blank=True)
    # gift option
    gift_option = models.BooleanField(default=False)
    gift_recipient = models.CharField(max_length=80, null=True, blank=True)
    gift_message = models.TextField(max_length=1000, null=True, blank=True)
    # totals
    total = models.DecimalField(max_digits=10, decimal_places=2,
                                null=False, default=0)
    # shopping bag
    bag = models.TextField(null=False, blank=False, default='')
    # paiement
    transaction_id = models.CharField(max_length=1000, null=True, blank=True)
    paid = models.BooleanField(default=False)
    # status
    status = models.CharField(max_length=15, choices=STATUS,
                              default=IN_PROGRESS)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total via signal each time a line item is added
        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))[
                     'lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Stores details for each line of products attached to the order
    Related to Order and Artwork models
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    artwork = models.ForeignKey(Artwork, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='lineartworks')
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.artwork.on_sale:
            price = self.artwork.sale_price
        else:
            price = self.artwork.price
        self.lineitem_total = price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """Display string"""
        return f'{self.artwork.name} on order {self.order.order_number}'
