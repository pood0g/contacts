from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact
from re import sub


class ContactDetailsForm(forms.ModelForm):
    
    class Meta:
        exclude = ["owner", "slug"]
        model = Contact

    firstname = forms.RegexField(
        regex=r"^[a-zA-Z]+$",
        max_length=40,
        label="First Name",
        error_messages={
            "invalid": "Firstname must consist only letters A-Z and a-z",
            },
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter first name",
                "class": "form-control",
                }),
                )
    lastname = forms.RegexField(
        regex=r"^[a-zA-Z]+$",
        max_length=40,
        label="Last Name",
        error_messages={
            "invalid": "Lastname must consist only letters A-Z and a-z",
            },
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter last name",
                "class": "form-control",
                }),
                )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email address",
                "class": "form-control",
                }),
                )
    phone = forms.RegexField(
        regex=r"[\d\(\)\-\s\+]+",
        label="Phone Number",
        error_messages={"invalid": "Phone Number may only contain digits and \"+ - ( )\" characters"},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter phone number",
                "class": "form-control",
                }),
                )

    def clean(self):
        phone = sub(r"[^\d\+]", "",self.cleaned_data['phone'])
        if phone[:2] == "04" and len(phone) == 10:
            self.cleaned_data['phone'] = f"{phone[:4]} {phone[4:7]} {phone[7:]}"
        elif phone.startswith('+') and len(phone) == 11:
            self.cleaned_data['phone'] = f"+{phone[1:3]} {phone[3]} {phone[4:8]} {phone[8:]}"
        elif phone[:2] in ["02", "03", "07", "08"] and len(phone) == 10:
            self.cleaned_data['phone'] = f"({phone[:2]}) {phone[2:6]} {phone[6:]}"


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
