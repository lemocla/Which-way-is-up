"""
Test cases for profile app
"""

from django.test import TestCase

from django.contrib.auth.models import User
from artworks.models import Artwork, ShopCategory
from checkout.models import Order


class ProfilesViewTest(TestCase):
    """
    Class to test profiles views
    """
    def setUp(self):
        """Set test data for user, category and artwork"""
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email='testuser@test.com',
                        password='12345')

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
                        display_shop=True,
                      )

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
            status="in progress",
        )

    def test_profile_view_url_exists(self):
        """
        Check url response for profile page
        """
        response = self.client.get('/my_profile/')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)

    def test_order_history_view_url_exists(self):
        """
        Check url response for order history
        """
        response = self.client.get('/my_profile/order_history')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)

    def test_order_detail_view_url_exists(self):
        """
        Check url response for order detail
        """
        response = self.client.get(
                    f'/my_profile/order_details/{self.order.order_number}')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)

    def test_my_reviews_view_url_exists(self):
        """
        Check url response for my reviews
        """
        response = self.client.get('/my_profile/my_reviews')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)

    def test_wishlist_view_url_exists(self):
        """
        Check url response for my wishlist
        """
        response = self.client.get('/my_profile/wishlist/')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)

    def test_add_to_wishlist_view_url_exists(self):
        """
        Check url response for add to wishlist
        """
        response = self.client.get(
                    f'/my_profile/add_to_wishlist/{self.artwork.id}')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_remove_from_wishlist_view_url_exists(self):
        """
        Check url response for removing from wishlist
        """
        response = self.client.get(
                    f'/my_profile/remove_from_wishlist/{self.artwork.id}')
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 302)
