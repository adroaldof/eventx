# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError

from core.models import Speaker, Contact


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


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )

    def test_email(self):
        'Test contact email'
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='E',
            value='test@testing.com'
        )
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        'Test contact phone'
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='P',
            value='12-123456789'
        )
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        'Test contact fax'
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='E',
            value='12-234567890'
        )
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Contact kind should be limited to E, P or F'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'Contact string representation should be value'
        contact = Contact(
            speaker=self.speaker,
            kind='E',
            value='test@testing.com'
        )
        self.assertEqual('test@testing.com', unicode(contact))
