from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact
from re import sub


class ContactDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude = ["owner"]

    firstname = forms.RegexField(
        regex=r"^[a-zA-Z]+$",
        max_length=40,
        label="First Name",
        error_messages={
            "invalid": "Firstname must consist only letters A-Z and a-z",
            },
        widget=forms.TextInput(
            attrs={"placeholder": "Enter first name"}),
    )
    lastname = forms.RegexField(
        regex=r"^[a-zA-Z]+$",
        max_length=40,
        label="Last Name",
        error_messages={
            "invalid": "Lastname must consist only letters A-Z and a-z",
            },
        widget=forms.TextInput(
            attrs={"placeholder": "Enter last name"}),
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter email address"})
    )
    phone = forms.RegexField(
        regex=r"[\d\(\)\-\s\+]+",
        label="Phone Number",
        error_messages={"invalid": "Phone Number may only contain digits and (,+,-,) characters"},
        widget=forms.TextInput(attrs={"placeholder": "Enter phone number"}),
    )

    def clean(self):
        phone = sub(r"[^\d]", "",self.cleaned_data['phone'])
        if phone[:2] == "04" and len(phone) == 10:
            self.cleaned_data['phone'] = f"{phone[:4]} {phone[4:7]} {phone[7:]}"

class SearchContactsForm(forms.Form):
    query = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search",
                "class": "form-control",
                }))

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
