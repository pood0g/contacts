from django.urls import path
from views import PasswordListView, PasswordDeleteView, PasswordUpdateView, PasswordAddView

urlpatterns = [
    path("/", PasswordListView.as_view(), name="pw_list"),
    path("add/", PasswordAddView.as_view(), name="pw_add"),
    path("delete/", PasswordDeleteView.as_view(), name="pw_delete"),
    path("/modify", PasswordUpdateView.as_view(), name="pw_modify")
]