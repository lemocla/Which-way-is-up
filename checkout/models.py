"""
Models for checkout app
- Order
"""

import uuid

from django.db import models
from django_countries.fields import CountryField
from profiles.models import UserProfile
from artworks.models import Artwork


class Order(models.Model):
    """
    Model for checkout orders
    """
    class Meta:
        """Order by date"""
        ordering = ['date']

    IN_PROGRESS = 'in progress'
    DISPATCHED = 'dispatched'

    STATUS = [
        (IN_PROGRESS, 'in progress'),
        (DISPATCHED, 'disptached'),
    ]

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
                                    blank=False)
    delivery_postcode = models.CharField(max_length=20, null=True, blank=True)
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
                                   blank=False)
    billing_postcode = models.CharField(max_length=20, null=True, blank=True)
    # gift option
    gift_option = models.BooleanField(default=False)
    gift_recipient = models.CharField(max_length=50, null=True, blank=True)
    gift_message = models.TextField(max_length=1000, null=True, blank=True)
    # totals
    total = models.DecimalField(max_digits=10, decimal_places=2,
                                null=False, default=0)
    # shopping bag
    bag = models.TextField(null=False, blank=False, default='')
    # status
    status = models.CharField(max_length=15, choices=STATUS,
                              default=IN_PROGRESS)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

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
    Model for each line of products attached to the order
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    artwork = models.ForeignKey(Artwork, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.artwork.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.artwork.name} on order {self.order.order_number}'
