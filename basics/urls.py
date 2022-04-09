from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("people/", views.contacts_page, name="contacts"),
    path("add/", views.AddContactView.as_view(), name="add"),
    path("delete/<int:pk>/", views.DeleteContactView.as_view(), name="delete"),
    path("update/<int:pk>/", views.UpdateView.as_view(), name="update"),
    path("register/", views.register_user, name="register"),
]