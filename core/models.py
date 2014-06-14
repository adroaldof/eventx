# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import KindContactManager, PeriodManager


class Speaker(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_('Description'), blank=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})


class Contact(models.Model):
    KINDS = (
        ('P', _('Phone')),
        ('E', _('Email')),
        ('F', _('Fax')),
    )
    speaker = models.ForeignKey('Speaker', verbose_name=_('Speaker'))
    kind = models.CharField(_('Kind'), max_length=1, choices=KINDS)
    value = models.CharField(_('Value'), max_length=255)

    objects = models.Manager()
    emails = KindContactManager('E')
    faxes = KindContactManager('F')
    phones = KindContactManager('P')

    def __unicode__(self):
        return self.value


class Talk(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))
    start_time = models.TimeField(_('Time'), blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('Speakers'))

    objects = PeriodManager()

    class Meta:
        verbose_name = _('Talk')
        verbose_name_plural = _('Talks')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('core:talk', (), {'pk': self.pk})

    @property
    def slides(self):
        return self.media_set.filter(kind='SS')

    @property
    def videos(self):
        return self.media_set.filter(kind='YT')


class Course(Talk):
    slots = models.IntegerField(_('Slots'))
    notes = models.TextField(_('Notes'))

    objects = PeriodManager()


class Media(models.Model):
    MEDIAS = (
        ('YT', _('YouTube')),
        ('SS', _('SlideShare')),
    )

    talk = models.ForeignKey('Talk', verbose_name=_('Talk'))
    kind = models.CharField(_('Kind'), max_length=2, choices=MEDIAS)
    title = models.CharField(_('Title'), max_length=255)
    media_id = models.CharField(_('Reference'), max_length=255)

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)
