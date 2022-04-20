from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import RegisterUserForm, UserLoginForm


class RegisterUserView(FormView):
    form_class = RegisterUserForm
    success_url = reverse_lazy("home")
    template_name = "register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "User Registered Successfully")
        return redirect("home")
    
    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, f"{error.as_text().strip('* ')}")
        return super().form_invalid(form)

class UserLoginView(FormView):
    form_class = UserLoginForm
    success_url = reverse_lazy("home")
    template_name = 'login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, f"{error.as_text().strip('* ')}")
        return super().form_invalid(form)