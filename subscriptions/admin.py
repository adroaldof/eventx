# coding: utf-8
from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import ugettext as _

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User Info'), {'fields': ('name', 'cpf')}),
        (_('Contact Info'), {'fields': ('email', 'phone', 'paid')}),
    )
    list_display = (
        'name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today',
        'paid'
    )
    search_fields = ('name', 'email', 'phone', 'created_at')
    ordering = ('name', 'email')
    date_hierarchy = 'created_at'
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = _('Subscribed today?')
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)
