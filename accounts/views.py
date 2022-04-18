from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterUserForm


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "User Registered Successfully")
            return redirect("listing")
        messages.error(request, "Registration Failed")

    context = {
        "registration_form": RegisterUserForm()
    }
    return render(request, "registration/register.html", context)
