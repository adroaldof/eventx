from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from .models import Subscription


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_('CPF must have only digits'))

    if len(value) != 11:
        raise ValidationError(_('CPF must have eleven digits'))


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].validators.append(CPFValidator)
