# coding: utf-8
from django.test import TestCase
from core.models import Talk, Media


class MediaModelTest(TestCase):
    def setUp(self):
        talk = Talk.objects.create(
            title='Test Talk Media',
            start_time='10:00'
        )
        self.media = Media.objects.create(
            talk=talk,
            kind='YT',
            media_id='QjA5faZF1A8',
            title='Video'
        )

    def test_create(self):
        'Test media creation'
        self.assertEqual(1, self.media.pk)

    def test_unicode(self):
        'String media representation should be talk title and video title'
        self.assertEqual('Test Talk Media - Video', unicode(self.media))
