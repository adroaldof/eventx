# coding: utf-8
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Speaker, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Speaker Info'), {'fields': ('name', 'slug', 'url', )}),
        (_('Speaker Description'), {'fields': ('description', )}),
    )
    list_display = ('name', 'url', )
    inlines = [ContactInline, ]
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Speaker, SpeakerAdmin)
