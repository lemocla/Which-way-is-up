"""
Test cases for homepage
"""
from django.test import TestCase
from django.urls import reverse
from portfolio.models import Portfolio
from reviews.models import Review


class HomeViewTest(TestCase):
    """
    Class to test home views
    """
    def test_view_url_exists(self):
        """
        Check url response for index
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_and_template(self):
        """
        Check return home views and right template
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_view_url_accessible_by_name(self):
        """
        Check url accessible by name and right template
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_view_url_get_portfolio_and_reviews(self):
        """
        Check home context, name and template
        """
        response = self.client.get(reverse('home'))
        # Get portfolio item
        portfolio_initial = Portfolio.objects.filter(homepage=True)
        if len(portfolio_initial) > 0:
            portfolio = portfolio_initial[0]
            self.assertTrue(len(portfolio) == 1)
        else:
            portfolio = None
            self.assertTrue(portfolio is None)

        # Get 3 latest top reviews
        reviews = Review.objects.all().order_by('-ratings', '-created_at')[:3]

        self.assertEqual(response.context['portfolio'], portfolio)
        self.assertCountEqual(response.context['reviews'], reviews)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
