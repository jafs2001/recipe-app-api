"""
Test custom Django management commands.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_wemail_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = '123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['TEst1@eXample.COM', 'TEst1@example.com'],
            ['TEST3@eXample.COM', 'TEST3@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_email_needed(self):
        """Test user cannot be created without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser('email@gmail.com', 'pw')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
