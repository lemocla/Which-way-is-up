"""
Test cases for checkout app
"""
from django.test import TestCase
from django.urls import reverse, resolve
from .models import Order


class CheckoutViewTest(TestCase):
    """
    Class to test checkout views
    """
    def setUp(self):
        """Set test data for user and artwork"""
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

    def test_checkout_view_url_exists(self):
        """
        Check url response and template for checkout page
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_checkout_view_url_accessible_by_name_exists(self):
        """
        Check checkout url accessible by name and right template
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_success_view_url_accessible_by_name_exists(self):
        """
        Check checkout success url accessible by name and right template
        """
        url = f'/checkout/checkout_success/{self.order.order_number}'
        found = resolve(url)
        self.assertEqual(found.url_name, "checkout_success")
