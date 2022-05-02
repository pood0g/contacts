from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CalendarView(TemplateView, LoginRequiredMixin):
    template_name = 'calendar.html'