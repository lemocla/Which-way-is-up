"""
Test cases for contact app
"""
from django.test import TestCase
from django.urls import reverse


class ContactViewTest(TestCase):
    """
    Class to test contact views
    """
    def test_contact_view_url_exists(self):
        """
        Check url response and template for contact page
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_view_url_accessible_by_name_exists(self):
        """
        Check checkout url accessible by name and right template
        """
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertEqual(response.status_code, 200)
