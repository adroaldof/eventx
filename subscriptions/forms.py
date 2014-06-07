from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.core.validators import EMPTY_VALUES

from .models import Subscription


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_('CPF must have only digits'))

    if len(value) != 11:
        raise ValidationError(_('CPF must have eleven digits'))


class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (forms.TextInput(attrs=attrs), forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')


class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (forms.IntegerField(), forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if not data_list:
            return ''

        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(_('Area code must be provided'))

        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(_('Invalid number'))

        return '%s-%s' % tuple(data_list)


class SubscriptionForm(forms.ModelForm):
    phone = PhoneField(label=_('Phone'), required=False)

    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].validators.append(CPFValidator)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = map(lambda w: w.capitalize(), name.split())
        capitalized_name = ' '.join(words)
        return capitalized_name

    def clean(self):
        super(SubscriptionForm, self).clean()
        cleaned = self.cleaned_data

        if not cleaned.get('email') and not cleaned.get('phone'):
            raise ValidationError(_('Either email or phone must be informed'))

        return self.cleaned_data
