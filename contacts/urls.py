from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactsView.as_view(), name="listing"),
    path("add/", views.AddContactView.as_view(), name="add"),
    path("delete/<slug:slug>/", views.DeleteContactView.as_view(), name="delete"),
    path("modify/<slug:slug>/", views.ModifyContactView.as_view(), name="modify"),
]