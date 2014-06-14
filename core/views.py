# coding: utf-8
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from core.models import Speaker, Talk


def home(request):
    return TemplateResponse(request, 'index.html', {})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return TemplateResponse(request, 'core/speaker_detail.html', {
        'speaker': speaker
    })


def talk_list(request):
    args = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return TemplateResponse(request, 'core/talk_list.html', args)
