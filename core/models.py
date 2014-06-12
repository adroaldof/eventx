# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_('Description'), blank=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    KINDS = (
        ('P', _('Phone')),
        ('E', _('Email')),
        ('F', _('Fax')),
    )
    speaker = models.ForeignKey('Speaker', verbose_name=_('Speaker'))
    kind = models.CharField(_('Kind'), max_length=1, choices=KINDS)
    value = models.CharField(_('Value'), max_length=255)

    def __unicode__(self):
        return self.value
