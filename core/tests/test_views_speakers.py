# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from core.models import Speaker


class SpeakersViewTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )
        self.resp = self.client.get(r('core:speakers'))

    def test_get(self):
        'GET speakers should return 200 status code'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speakers.html'
        self.assertTemplateUsed(self.resp, 'core/speakers.html')

    def test_html(self):
        self.assertContains(self.resp, 'palestrante/test-testing')
        self.assertContains(self.resp, 'Test Testing')
        self.assertContains(self.resp, 'http://testing.test.com')
