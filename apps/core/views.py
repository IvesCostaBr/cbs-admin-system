from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.collaborator.models import Collaborator


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'core/home_page.html'