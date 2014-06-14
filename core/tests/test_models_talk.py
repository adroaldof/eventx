# coding: utf-8
from django.test import TestCase

from core.managers import PeriodManager
from core.models import Talk, Course


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


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            description='Test Course Description',
            title='Test Course Title',
            start_time='09:00',
            slots=20
        )

    def test_create(self):
        'Test if course were created'
        self.assertEqual(1, self.course.pk)

    def test_unicode(self):
        'Course string representation should be its title'
        self.assertEqual('Test Course Title', unicode(self.course))

    def test_speakers(self):
        'Course has many Speakers and vice-versa'
        self.course.speakers.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )

    def test_period_manager(self):
        'Course default manager must be instance of PeriodManager'
        self.assertIsInstance(Course.objects, PeriodManager)
