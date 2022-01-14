from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString
from base64 import b64encode
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .. import views

register = template.Library()

@register.filter(name='artistP')
@stringfilter
def artistP(name):
    print(name)
    return views.artist(name)