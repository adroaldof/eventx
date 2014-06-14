# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from core.models import Speaker, Talk


class TalkViewTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )
        t = Talk.objects.create(
            description='Talk Description',
            title='Talk Title',
            start_time='10:30'
        )
        t.speakers.add(s)
        self.resp = self.client.get(r('core:talk', args=[t.pk]))

    def test_get(self):
        'GET specific talk shoud return 200 status code'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template shoud be core/talk_detail.html'
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')

    def test_html(self):
        'HTML shoud list talk'
        self.assertContains(self.resp, 'Talk Title')
        self.assertContains(self.resp, 'Talk Description')
        self.assertContains(self.resp, '10:30')
        self.assertContains(self.resp, 'Test Testing')
        self.assertContains(self.resp, '/palestrante/test-testing')

    def test_talk_in_context(self):
        'Talk instance shoud be in context'
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_no_found(self):
        'Talk intance that does not exists shoud get 404 status code'
        resp = self.client.get(r('core:talk', args=[0]))
        self.assertEqual(404, resp.status_code)
