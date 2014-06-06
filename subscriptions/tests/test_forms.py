from django.test import TestCase

from subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        'Form must have four fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF must accept only digits'
        form = self.make_validated_form(cpf='AAAAA678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_eleven_digits(self):
        'CPF must have eleven digits'
        form = self.make_validated_form(cpf='12345')
        self.assertItemsEqual(['cpf'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(
            name='Test Testing Name',
            cpf='12345678901',
            email='test@testing.com',
            phone='12-123456789'
        )
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
