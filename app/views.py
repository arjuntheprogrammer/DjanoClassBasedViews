# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.timezone import now 

class AboutUsView(TemplateView):
    template_name = 'about_us.html'

def get_context_data(self, **kwargs):
    context = super(AboutUsView, self).get_context_data(**kwargs)
    context['now'] = now().weekday
    print now().weekday()
    print now().hour()

    if now().weekday() < 5 and 8< now().hour < 18:
        context['open'] = True
    else: 
        context['open'] = False
    return context
