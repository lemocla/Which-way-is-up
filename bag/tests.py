"""
Test cases for bag app
"""

from django.test import TestCase
from django.urls import reverse, resolve

from artworks.models import Artwork, ShopCategory


class BagViewTest(TestCase):
    """
    Class to test bag views
    """
    def setUp(self):
        """Set test data for user and artwork"""

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

    def test_bag_view_url_exists(self):
        """
        Check url response and template for bag page
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_bag_view_url_accessible_by_name_exists(self):
        """
        Check bag url accessible by name and right template
        """
        response = self.client.get(reverse('bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag_view_url_exists(self):
        """
        Test view add to bag
        """
        url = f'/bag/add/{self.artwork.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "add_to_bag")

    def test_adjust_bag_view_url_exists(self):
        """
        Test view adjust bag
        """
        url = f'/bag/adjust/{self.artwork.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "adjust_bag")

    def test_remove_from_bag_view_url_exists(self):
        """
        Test view remove from bag
        """
        url = f'/bag/remove/{self.artwork.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "remove_from_bag")

    def test_gift_option_view_url_exists(self):
        """
        Test view gift option
        """
        response = self.client.get('/bag/gift_option/')
        self.assertEqual(response.status_code, 200)
