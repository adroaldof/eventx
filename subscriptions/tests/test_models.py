# coding: utf-8
from datetime import datetime
from django.test import TestCase
from django.db import IntegrityError

from subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Test Testing Name',
            cpf='12345678901',
            email='test@testing.com',
            phone='12-123456789'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Subscription must have a automatic created_at field'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        'Verify subscriber name'
        self.assertEqual(u'Test Testing Name', unicode(self.obj))

    def test_paid_default_value_is_false(self):
        'By default paid must be False'
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force collision on cpf unique test
        Subscription.objects.create(
            name='Test Testing Name',
            cpf='12345678901',
            email='test@testing.com',
            phone='12-123456789'
        )

    def test_cpf_unique(self):
        'CPF field must be unique'
        subsc = Subscription(
            name='Test Testing Same CPF',
            cpf='12345678901',
            email='test.other@testing.com',
            phone='12-123456789'
        )
        self.assertRaises(IntegrityError, subsc.save)

    def test_email_unique(self):
        'Email field must be unique'
        subsc = Subscription(
            name='Test Testing Same Email',
            cpf='88888888888',
            email='test@testing.com',
            phone='12-123456789'
        )
        self.assertRaises(IntegrityError, subsc.save)
