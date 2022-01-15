"""
Test cases for artworks app
"""

from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Artwork, ShopCategory


class ArtworkViewTest(TestCase):
    """
    Class to test artwork views
    """
    def setUp(self):
        """Set test data for user and artwork"""
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

    def test_shop_view_url_exists(self):
        """
        Check url response and template for shop pages
        """
        response = self.client.get('/artworks/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artworks/artworks.html')

    def test_shop_view_url_accessible_by_name_exists(self):
        """
        Check shop url accessible by name and right template
        """
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artworks/artworks.html')

    def test_artwork_detail_view_url_exists(self):
        """
        Check url response and template for artwork detail
        """
        response = self.client.get(f'/artworks/{self.artwork.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artworks/artwork_detail.html')

    def test_add_artwork_view_url_exists(self):
        """
        Test view add artwork
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(reverse('add_artwork'))
        self.assertEqual(response.status_code, 302)

    def test_edit_artwork_view_url_exists(self):
        """
        Test view edit artwork
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(f'/artworks/edit/{self.artwork.id}/')
        self.assertEqual(response.status_code, 302)

    def test_delete_artwork_view_url_exists(self):
        """
        Test view delete artwork
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(f'/artworks/delete/{self.artwork.id}/')
        self.assertEqual(response.status_code, 302)
