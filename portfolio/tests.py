"""
Test cases for portfolio app
"""

from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Portfolio, PortfolioCategory


class PortfolioViewTest(TestCase):
    """
    Class to test portfolio views
    """
    def setUp(self):
        """Set test data for user and portfolio"""
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email='testuser@test.com',
                        password='12345')

        self.category = PortfolioCategory.objects.create(
                        name="test case")

        self.portfolio = Portfolio.objects.create(
            name="test porfolio",
            image=None,
            description="test",
            materials="test",
            category=self.category,
            status="active",
            homepage=False)

    def test_portfolio_detail_view_url_exists(self):
        """
        Check url response and template for portfolio detail page
        """
        response = self.client.get(f'/portfolio/{self.portfolio.id}/')
        self.assertEqual(response.status_code, 200)

    def test_add_portfolio_view_url_exists(self):
        """
        Test view add portfolio
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(reverse('add_portfolio'))
        self.assertEqual(response.status_code, 302)

    def test_edit_portfolio_view_url_exists(self):
        """
        Test view edit portfolio
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(f'/portfolio/edit/{self.portfolio.id}/')
        self.assertEqual(response.status_code, 302)

    def test_delete_portfolio_view_url_exists(self):
        """
        Test view delete portfolio
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(f'/portfolio/delete/{self.portfolio.id}/')
        self.assertEqual(response.status_code, 302)
