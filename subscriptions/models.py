from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    name = models.CharField(_('name'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    email = models.EmailField(_('email'), blank=True)
    phone = models.CharField(_('phone'), max_length=20, blank=True)
    paid = models.BooleanField(_('paid'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')

    def __unicode__(self):
        return self.name
