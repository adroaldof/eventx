# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:home'))

    def test_get(self):
        'GET / must return get 200 status code'
        self.assertEqual(200, self.resp.status_code)
