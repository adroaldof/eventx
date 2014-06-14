# coding: utf-8
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Speaker, Contact, Talk, Course, Media


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


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1


class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', )
    inlines = [MediaInline, ]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slots', 'start_time', )


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Course, CourseAdmin)
