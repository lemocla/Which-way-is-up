"""
Test cases for about app
"""
import datetime
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Event


class AboutViewTest(TestCase):
    """
    Class to test about views
    """
    def setUp(self):
        """Set test data for user and event"""
        self.test_user = User.objects.create_user(
                        username='testuser',
                        email='testuser@test.com',
                        password='12345')

        self.event = Event.objects.create(
                     date_start=(datetime.date(2020, 5, 1)),
                     date_end=None,
                     place='test place',
                     description='test description')

    def test_about_view_url_exists(self):
        """
        Check url response and template for about
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_view_url_accessible_by_name(self):
        """
        Check about url accessible by name and right template
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')

    def test_add_event_view_url_exists(self):
        """
        Test view add event
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(reverse('add_event'))
        self.assertEqual(response.status_code, 302)

    def test_edit_event_view_url_exists(self):
        """
        Test view edit event
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(f'/about/edit/{self.event.id}/')
        self.assertEqual(response.status_code, 302)

    def test_delete_event_view_url_exists(self):
        """
        Test view delete event
        """
        login = self.client.login(username=self.test_user.username,
                                  password='12345')
        self.assertTrue(login)
        response = self.client.get(f'/about/delete/{self.event.id}/')
        self.assertEqual(response.status_code, 302)
