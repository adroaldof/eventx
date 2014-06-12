from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_('Description'), blank=True)

    def __unicode__(self):
        return self.name
