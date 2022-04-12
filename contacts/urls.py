from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("contacts/", views.contacts_page, name="contacts"),
    path("add/", views.AddContactView.as_view(), name="add"),
    path("delete/<slug:slug>/", views.DeleteContactView.as_view(), name="delete"),
    path("modify/<slug:slug>/", views.ModifyContactView.as_view(), name="modify"),
    path("register/", views.register_user, name="register"),
]