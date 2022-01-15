"""
Tests cases for Newsletter App
"""
from django.test import TestCase
from django.urls import reverse
from django.core import mail

from django.contrib.auth.models import User
from profiles.models import UserProfile

from .forms import SubscribeForm
from .models import Mailing


class TestNewsletterViews(TestCase):
    """
    Test views for newsletter app
    """
    def setUp(self):
        self.test_user = User.objects.create_user(
                        username='testcase',
                        email='testcasemail@test.com',
                        password='12345')

    def tearDown(self):
        # Clean up after each test
        self.test_user.delete()

    def test_get_add_to_mailing_list(self):
        """
        Test newsletter url
        """
        response = self.client.get(reverse('newsletter'))
        self.assertEqual(response.status_code, 302)

    def test_add_to_mailing_list_and_send_email(self):
        """
        Test form is valid and send temail
        """
        response = self.client.get(reverse('newsletter'))

        form_data = {'email_newsletter': 'testcasemail@test.com'}
        form = SubscribeForm(data=form_data)

        mail.send_mail(
            "hello",
            "thank you for signing for our newseletter",
            "admin@test.com",
            [form['email_newsletter']])
        self.assertTrue(form.is_valid())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(response.status_code, 302)

    def test_add_to_mailing_list_with_user_and_email(self):
        """
        Test form is valid, update user profile and send email
        """
        response = self.client.get(reverse('newsletter'))

        form_data = {'email_newsletter': 'testcasemail@test.com'}
        form = SubscribeForm(data=form_data)

        existing_user = self.test_user

        profile = UserProfile.objects.get(user=existing_user)
        self.assertFalse(profile.newsletter)
        profile.newsletter = True
        profile.save()
        self.assertTrue(profile.newsletter)

        mail.send_mail(
            "hello",
            "thank you for signing for our newseletter",
            "admin@test.com",
            [form['email_newsletter']])
        self.assertTrue(form.is_valid())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(response.status_code, 302)


class TestNewsletterForm(TestCase):
    """
    Test form for newsletter form
    """
    def setUp(self):
        """
        Create test object in mailing
        """
        Mailing.objects.create(email_newsletter="testcase@test.com")

    def test_form_is_valid(self):
        """
        Test form is valid
        """
        form_data = {'email_newsletter': 'testcase0@test.com'}
        form = SubscribeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_value_exists(self):
        """
        Test if email not not unique
        """
        form_data = {'email_newsletter': 'testcase@test.com'}
        form = SubscribeForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_input(self):
        """
        Test if input is invalid
        """
        form_data = {'email_newsletter': 'test'}
        form = SubscribeForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_empty(self):
        """
        Test if input is empty
        """
        form_data = {'email_newsletter': None}
        form = SubscribeForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_extra_long_string(self):
        """
        Test if input is empty
        """
        form_data = {'email_newsletter': (
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@test.com')}
        form = SubscribeForm(data=form_data)
        self.assertFalse(form.is_valid())
