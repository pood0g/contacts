from django.urls import path
from .views import AddContactView, DeleteContactView, ModifyContactView, ListContactsView

urlpatterns = [
    path("", ListContactsView.as_view(), name="contacts"),
    path("add/", AddContactView.as_view(), name="add"),
    path("delete/<slug:slug>/", DeleteContactView.as_view(), name="delete"),
    path("modify/<slug:slug>/", ModifyContactView.as_view(), name="modify"),
]