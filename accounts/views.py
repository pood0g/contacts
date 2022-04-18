from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import RegisterUserForm


class RegisterUserView(FormView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "User Registered Successfully")
        return redirect("home")

    def form_invalid(self, form):
        messages.error(self.request, "Registration Failed")