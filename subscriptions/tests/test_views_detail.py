from django.test import TestCase
from django.core.urlresolvers import reverse as r

from subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
            name='Test Testing Name',
            cpf='12345678901',
            email='test@testing.com',
            phone='12-12345678'
        )
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))

    def test_get(self):
        'GET /incricao/1/ should return status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses subscription detail template'
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_detail.html'
        )

    def test_context(self):
        'Context must have a subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered'
        self.assertContains(self.resp, 'Test Testing Name')


class DetailNotFound(TestCase):
    def test_not_found(self):
        'Check not found page if does not exists subscriptions'
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
