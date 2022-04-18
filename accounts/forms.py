from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):

    first_name = forms.RegexField(
        regex=r"^\w{1,150}$",
        required=True,
        max_length=150,
        label="First Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter first name",
                "class": "form-control",
                "pattern": "^[a-zA-Z]{1,50}$",
                }))

    last_name = forms.RegexField(
        regex=r"^\w{1,150}$",
        required=True,
        max_length=150,
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter last name",
                "class": "form-control",
                "pattern": "^[a-zA-Z]{1,50}$",
                }))
    
    email = forms.EmailField(
        required=True,
        max_length=80,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email address",
                "class": "form-control",
                "pattern": "^[\w\.]+@\w+\.(\w+\.?)+$"
                }))

    username = forms.RegexField(
        regex=r"^\w{1,150}$",
        required=True,
        max_length=150,
        widget=forms.TextInput({
            "placeholder": "Enter your username",
            "class": "form-control",
            "pattern": "^\w{1,150}$"
        }))


    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

    