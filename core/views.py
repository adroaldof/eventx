# coding: utf-8
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from core.models import Speaker


def home(request):
    return TemplateResponse(request, 'index.html', {})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return TemplateResponse(request, 'core/speaker_detail.html', {
        'speaker': speaker
    })
