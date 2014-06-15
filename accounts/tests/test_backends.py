# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.utils import override_settings
from unittest import skip

from accounts.backends import EmailBackend


@skip
class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='Test Testing',
            email='test@testing.com',
            password='testpassword'
        )
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        'Test authenticate with email'
        user = self.backend.authenticate(
            email='test@testing.com',
            password='testpassword'
        )
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        'Test wrong password'
        user = self.backend.authenticate(
            email='test@testing.com',
            password='wrong'
        )
        self.assertIsNone(user)

    def test_unknown_user(self):
        'Test unknown user'
        user = self.backend.authenticate(
            email='unknown@testing.com',
            password='unknown'
        )
        self.assertIsNone(user)

    def test_get_user(self):
        'Test get user'
        self.assertIsNotNone(self.backend.get_user(1))


@skip
class MultipleEmailTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='Test Testing 01',
            email='test@testing.com',
            password='testpassword'
        )
        UserModel.objects.create_user(
            username='Test Testing 02',
            email='test@testing.com',
            password='testpassword'
        )
        self.backend = EmailBackend()

    def test_multiple_email(self):
        'Test multiple emails'
        user = self.backend.authenticate(
            email='test@testing.com',
            password='wrong'
        )
        self.assertIsNone(user)


@skip
@override_settings(AUTHENTICATION_BACKENDS=('accounts.backends.EmailBackend',))
class FunctionEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='Test Testing',
            email='test@testing.com',
            password='testpassword'
        )
        self.backend = EmailBackend()

    def test_login_with_email(self):
        'Test login with email'
        result = self.client.login(
            email='test@testing.com',
            password='testpassword'
        )
        self.assertTrue(result)

    def test_login_with_username(self):
        'Test login with username'
        result = self.client.login(
            username='test@testing.com',
            password='testpassword'
        )
        self.assertTrue(result)
