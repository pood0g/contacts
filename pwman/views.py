from ast import Pass
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Passwords

class PasswordListView(ListView, LoginRequiredMixin):
    model = Passwords

class PasswordAddView(CreateView, LoginRequiredMixin):
    model = Passwords
    success_url = reverse_lazy('pw_list')

class PasswordDeleteView(DeleteView, LoginRequiredMixin):
    model = Passwords

class PasswordUpdateView(UpdateView, LoginRequiredMixin):
    model = Passwords
