from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "pattern": r"(?!^\d+$)^.{8,150}$",
                })
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "onkeyup": "passwordsMatch()"
                })
        self.fields['password2'].help_text = "Passwords must match"
        self.fields['password2'].label = "Verify Password"


    first_name = forms.RegexField(
        regex=r"^\w{1,150}$",
        required=True,
        max_length=150,
        label="First Name",
        help_text="Alpha characters only",
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "pattern": r"^[a-zA-Z]{1,50}$",
                }))

    last_name = forms.RegexField(
        regex=r"^\w{1,150}$",
        required=True,
        max_length=150,
        label="Last Name",
        help_text="Alpha characters only",
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "pattern": r"^[a-zA-Z]{1,50}$",
                }))
    
    email = forms.EmailField(
        required=True,
        max_length=80,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "pattern": r"^[\w\.]+@\w+\.(\w+\.?)+$"
                }))

    username = forms.RegexField(
        regex=r"^\w{4,150}$",
        required=True,
        max_length=150,
        help_text="Minimum 4 chars, Letters, Numbers and underscores only.",
        widget=forms.TextInput({
            "placeholder": "",
            "class": "form-control",
            "pattern": r"^[\S]{8,150}$",
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

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "pattern": r"^[\S]{4,150}$"
                })
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control",
                "pattern": r"(?!^\d+$)^.{8,150}$",
                })
        