# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from core.models import Speaker


class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )
        url = r('core:speaker_detail', kwargs={'slug': 'test-testing'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET should result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'HTML must contain data'
        self.assertContains(self.resp, 'Test Testing')
        self.assertContains(self.resp, 'Passionate testing developer!')
        self.assertContains(self.resp, 'http://testing.test.com')

    def test_context(self):
        'Speaker must be in context'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        'Speaker details not found'
        url = r('core:speaker_detail', kwargs={'slug': 'test-404'})
        resp = self.client.get(url)
        self.assertEqual(404, resp.status_code)
