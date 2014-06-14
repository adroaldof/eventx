# coding: utf-8
from django.test import TestCase

from core.models import Contact, Speaker, Talk


class ContactManagerTest(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(
            name='Test Testing',
            slug='test-testing',
            url='http://testing.test.com',
            description='Passionate testing developer!'
        )
        speaker.contact_set.add(
            Contact(kind='E', value='test@testing.com'),
            Contact(kind='P', value='12-123456789'),
            Contact(kind='F', value='12-234567890'),
        )

    def test_emails(self):
        'Test email queryset'
        qs = Contact.emails.all()
        expected = ['<Contact: test@testing.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phone(self):
        'Test phone queryset'
        qs = Contact.phones.all()
        expected = ['<Contact: 12-123456789>']
        self.assertQuerysetEqual(qs, expected)

    def test_fax(self):
        'Test fax queryset'
        qs = Contact.faxes.all()
        expected = ['<Contact: 12-234567890>']
        self.assertQuerysetEqual(qs, expected)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        'Morning talks should return only talks before 12:00'
        self.assertQuerysetEqual(
            Talk.objects.at_morning(), ['Morning Talk'], lambda t: t.title
        )

    def test_afternoon(self):
        'Afternoon talks should return only talks after 12:00'
        self.assertQuerysetEqual(
            Talk.objects.at_afternoon(), ['Afternoon Talk'], lambda t: t.title
        )
