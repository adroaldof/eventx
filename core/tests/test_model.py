from django.test import TestCase

from core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )
        self.speaker.save()

    def test_create(self):
        'Speaker instance should be saved'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string representation should be the name'
        self.assertEqual('Test Testing', unicode(self.speaker))
