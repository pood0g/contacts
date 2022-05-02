from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path("", include("home.urls")),
    path("contacts/", include("contacts.urls")),
    path("accounts/", include("accounts.urls")),
    path("calendar/", include('events.urls'))
]
