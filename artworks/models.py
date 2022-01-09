"""
Models to manage artwork and shop categories
"""
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db import models, transaction
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
from portfolio.fields import CaseInsensitiveCharField
from portfolio.models import Portfolio


class ShopCategory(models.Model):
    """
    Model for shop categories
    """
    class Meta:
        """Order by name"""
        ordering = ['created_at']
        verbose_name_plural = "Shop categories"

    name = CaseInsensitiveCharField(max_length=150, unique=True)
    backend_name = CaseInsensitiveCharField(max_length=150,
                                            null=True,
                                            blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            str_name = self.name
            self.backend_name = str_name.replace(' ', '_')
            return super(ShopCategory, self).save(*args, **kwargs)


class Artwork(models.Model):
    """
    Model for portfolio
    """
    class Meta:
        """Order by name"""
        ordering = ['name']

    ACTIVE = 'active'
    DRAFT = 'draft'
    INACTIVE = 'inactive'

    STATUS = [
        (ACTIVE, 'active'),
        (DRAFT, 'draft'),
        (INACTIVE, 'inactive'),
    ]

    name = CaseInsensitiveCharField(max_length=150, unique=True)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=500, verbose_name='size(cm)')
    materials = models.CharField(max_length=500)
    year = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0.00)])
    # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    stock = models.PositiveSmallIntegerField(default=0,
                                             validators=[
                                                MaxValueValidator(500),
                                                MinValueValidator(0)
                                             ])
    stock_alert = models.PositiveSmallIntegerField(null=True, blank=True)
    portfolio = models.ForeignKey(Portfolio,
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL)
    shop_category = models.ForeignKey('ShopCategory',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL)
    related_items = models.ManyToManyField("self", blank=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6,
                                     decimal_places=2,
                                     null=True,
                                     blank=True,
                                     validators=[
                                        MinValueValidator(0.00)
                                     ])
    rating = models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default=ACTIVE)
    display_shop = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_average_rating(self):
        """
        ratings
        """
        self.rating = self.artwork.all().aggregate(Avg("ratings"))[
                              'ratings__avg']
        self.save()

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.portfolio:
            if str(self.portfolio.category) == 'commission':
                self.display_shop = False

            if str(self.status) != 'active':
                with transaction.atomic():
                    users_wishlist = self.wishlist_artwork.all()
                    for profile in users_wishlist:
                        # Update user profile
                        profile.wishlist_items.remove(self)
                        profile.save()
                        # Notify user
                        subject = ("Notification: wishlist item no longer "
                                   "available")
                        body = render_to_string(
                            'artworks/email/wishlist_notification.txt',
                            {'artwork': self.name.capitalize()})
                        sender = settings.EMAIL_HOST_USER
                        recipients = [profile.user.email]
                        send_mail(subject, body, sender, recipients)
        return super(Artwork, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.lineartworks:
            self.status = 'inactive'
            self.save()
        else:
            self.delete()
