# coding: utf-8
from django.test import TestCase

from core.managers import PeriodManager
from core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Intro to Tests',
            description='Long description on tests',
            start_time='10:30'
        )

    def test_create(self):
        'Test to verify if talk were created'
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        'Talk string representation should be its title'
        self.assertEqual('Intro to Tests', unicode(self.talk))

    def test_speakers(self):
        'Talk has meany Speakers and vice-versa'
        self.talk.speakers.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        'Talk default manager must be instance of PeriodManager'
        self.assertIsInstance(Talk.objects, PeriodManager)
