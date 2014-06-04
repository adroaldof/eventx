# coding: utf-8
from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import ungettext, ugettext as _

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

    actions = ['mark_as_paid', ]

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = _('Subscribed today?')
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = ungettext(
            '%d subscription was marked as paid',
            '%d subscriptions ware marked as paid',
            count
        )

        self.message_user(request, msg % count)

    mark_as_paid.short_description = _('Mark as paid')


admin.site.register(Subscription, SubscriptionAdmin)
