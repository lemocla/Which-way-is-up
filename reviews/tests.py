"""
Test cases for profile app
"""

from django.test import TestCase

from django.contrib.auth.models import User
from artworks.models import Artwork, ShopCategory
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from .models import Review


class ProfilesViewTest(TestCase):
    """
    Class to test profiles views
    """
    def setUp(self):
        """Set test data for user"""
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email='testuser@test.com',
                        password='12345')

        self.user_profile = UserProfile.objects.get(user=self.test_user)

        self.category = ShopCategory.objects.create(
                        name="test case")

        self.artwork = Artwork.objects.create(
                        name="test item",
                        image=None,
                        size="40 x 40",
                        materials="test",
                        year="2021",
                        price="10.00",
                        stock="6",
                        stock_alert="5",
                        portfolio=None,
                        shop_category=self.category,
                        on_sale=False,
                        sale_price=None,
                        rating=None,
                        status="active",
                        display_shop=True,)

        self.artwork2 = Artwork.objects.create(
                        name="test item 2",
                        image=None,
                        size="40 x 40",
                        materials="test",
                        year="2021",
                        price="10.00",
                        stock="6",
                        stock_alert="5",
                        portfolio=None,
                        shop_category=self.category,
                        on_sale=False,
                        sale_price=None,
                        rating=None,
                        status="active",
                        display_shop=True,)

        self.order = Order.objects.create(
            full_name="test test",
            email="testcase@test.com",
            phone_number="0000 0000",
            delivery_street_address1="test",
            delivery_street_address2="test",
            delivery_town_or_city="test",
            delivery_county="test",
            delivery_country="GB",
            delivery_postcode="test",
            billing_same_as_delivery=True,
            billing_street_address1="test",
            billing_street_address2="test",
            billing_town_or_city="test",
            billing_county="test",
            billing_country="GB",
            billing_postcode="test",
            gift_option=False,
            gift_recipient=None,
            gift_message=None,
            total=10.00,
            paid=True,
            status="in progress",)

        self.order_line = OrderLineItem.objects.create(
            order=self.order,
            artwork=self.artwork,
            quantity=1,
            lineitem_total=10.00)

        self.order_line2 = OrderLineItem.objects.create(
            order=self.order,
            artwork=self.artwork2,
            quantity=1,
            lineitem_total=10.00)

        self.review = Review.objects.create(
            ratings=5,
            comments="test",
            user_profile=self.user_profile,
            order_line=self.order_line,
            artwork=self.artwork)

    def test_reviews_view_url_exists(self):
        """
        Check url response for profile page
        """
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_add_review_url_exists(self):
        """
        Check url response for order history
        """
        response = self.client.get(
                    (f'/reviews/add_reviews/{self.artwork2.id}'
                     f'/{self.order_line2.id}/')
                )
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)

    def test_edit_review_view_url_exists(self):
        """
        Check url response for order detail
        """
        response = self.client.get(
                    f'/reviews/edit_reviews/{self.review.id}/')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)

    def test_delete_view_url_exists(self):
        """
        Check url response for my reviews
        """
        response = self.client.get(
                    f'/reviews/delete_reviews/{self.review.id}/')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)
