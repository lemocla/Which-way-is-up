"""
Test cases for policies app
"""
from django.test import TestCase
from django.urls import reverse


class PoliciesViewTest(TestCase):
    """
    Class to test policies views
    """
    def test_privacy_view_url_exists(self):
        """
        Check url response and template for privacy page
        """
        response = self.client.get('/policies/privacy')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'policies/privacy.html')

    def test_privacy_view_url_accessible_by_name_exists(self):
        """
        Check privacy policy url accessible by name and right template
        """
        response = self.client.get(reverse('privacy'))
        self.assertTemplateUsed(response, 'policies/privacy.html')
        self.assertEqual(response.status_code, 200)

    def test_accessibility_view_url_exists(self):
        """
        Check url response and template for accessibility page
        """
        response = self.client.get('/policies/accessibility')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'policies/accessibility.html')

    def test_accessibility_view_url_accessible_by_name_exists(self):
        """
        Check accessibility url accessible by name and right template
        """
        response = self.client.get(reverse('accessibility'))
        self.assertTemplateUsed(response, 'policies/accessibility.html')
        self.assertEqual(response.status_code, 200)

    def test_delivery_and_returns_view_url_exists(self):
        """
        Check url response and template for delivery and returns page
        """
        response = self.client.get('/policies/delivery_and_returns')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'policies/delivery_and_returns.html')

    def test_delivery_and_return_view_url_accessible_by_name_exists(self):
        """
        Check delivery and resturns url accessible by name and right template
        """
        response = self.client.get(reverse('delivery_and_returns'))
        self.assertTemplateUsed(response, 'policies/delivery_and_returns.html')
        self.assertEqual(response.status_code, 200)

    def test_terms_and_conditions_view_url_exists(self):
        """
        Check url response and template for terms and conditions page
        """
        response = self.client.get('/policies/terms_and_conditions')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'policies/terms_and_conditions.html')

    def test_terms_and_conditions_view_url_accessible_by_name_exists(self):
        """
        Check terms and conditions url accessible by name and right template
        """
        response = self.client.get(reverse('terms_and_conditions'))
        self.assertTemplateUsed(response, 'policies/terms_and_conditions.html')
        self.assertEqual(response.status_code, 200)
