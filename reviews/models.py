"""
Models for reviews app
"""

from django.db import models
from profiles.models import UserProfile
from checkout.models import OrderLineItem
from artworks.models import Artwork


class Review(models.Model):
    """
    Model for portfolio
    """
    class Meta:
        """Order by name"""
        ordering = ['created_at']

    RATINGS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    ratings = models.IntegerField(choices=RATINGS, default=5)
    comments = models.TextField(max_length=1500)
    user_profile = models.ForeignKey(UserProfile, null=True,
                                     on_delete=models.SET_NULL,
                                     related_name='reviews')
    order_line = models.ForeignKey(OrderLineItem, blank=True, null=True,
                                   on_delete=models.SET_NULL,
                                   related_name='orderline')
    artwork = models.ForeignKey(Artwork, null=True, on_delete=models.SET_NULL,
                                related_name='artwork')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.artwork} - {self.ratings}'
