"""
Models configuration for Profiles application
"""

from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from artworks.models import Artwork


class UserProfile(models.Model):
    """
    Stores user details and default delivery information
    Related to Artwork models
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=35, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True,
                           max_length=50)
    newsletter = models.BooleanField(default=False)
    wishlist_items = models.ManyToManyField(Artwork, blank=True,
                                            related_name='wishlist_artwork')

    def __str__(self):
        """username as string"""
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """

    if created:
        UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
    instance.userprofile.save()
