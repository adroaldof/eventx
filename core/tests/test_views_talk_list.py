# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from core.models import Speaker, Talk


class TalkListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )
        t1 = Talk.objects.create(
            description='Talk Description',
            title='Talk Title',
            start_time='10:30'
        )
        t2 = Talk.objects.create(
            description='Talk Description',
            title='Talk Title',
            start_time='15:00'
        )
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET talk list must return 200 status code'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template shoud be core/talk_list.html'
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        'HTML shoud list talks'
        self.assertContains(self.resp, 'Talk Title', 2)
        self.assertContains(self.resp, '10:30')
        self.assertContains(self.resp, '3')
        self.assertContains(self.resp, '/palestra/1/')
        self.assertContains(self.resp, '/palestra/2/')
        self.assertContains(self.resp, '/palestrante/test-testing', 2)
        self.assertContains(self.resp, 'Passionate testing developer!', 2)
        self.assertContains(self.resp, 'Test Testing', 2)
        self.assertContains(self.resp, 'Talk Description', 2)

    def test_morning_talks_in_context(self):
        'Test if morning talks is in context'
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks_in_context(self):
        'Test if afternoon talks is in context'
        self.assertIn('afternoon_talks', self.resp.context)
