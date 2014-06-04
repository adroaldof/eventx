# coding: utf-8
from django.test import TestCase
from mock import Mock

from subscriptions.admin import SubscriptionAdmin, Subscription, admin


class MarkAsPaidTest(TestCase):
    def setUp(self):
        # Make an Admin model instance
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        # Populate data base
        Subscription.objects.create(
            name='Test Testing Name',
            cpf='12345678901',
            email='test@testing.com',
            phone='12-123456789'
        )

    def test_has_action_mark_as_paid(self):
        'Action mark as paid is installed'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'Mark all as paid'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())