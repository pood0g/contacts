from django import forms
from .models import Contact
from re import sub


class ContactDetailsForm(forms.ModelForm):
    
    class Meta:
        exclude = ["owner", "slug"]
        model = Contact

    firstname = forms.RegexField(
        regex=r"^[a-zA-Z]+$",
        max_length=50,
        label="First Name",
        help_text="First name must consist only uppercase and lowercase letters.",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter first name",
                "class": "form-control",
                "pattern": "^[a-zA-Z]{1,50}$",
                }))

    lastname = forms.RegexField(
        regex=r"^[a-zA-Z]+$",
        max_length=50,
        label="Last Name",
        help_text="Last name must consist only uppercase and lowercase letters.",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter last name",
                "class": "form-control",
                "pattern": "^[a-zA-Z]{1,50}$",
                }))

    email = forms.EmailField(
        label="Email Address",
        max_length=80,
        help_text="Enter a valid email address.",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email address",
                "class": "form-control",
                "pattern": "^[\w\.]+@\w+\.(\w+\.?)+$"
                }))

    phone = forms.RegexField(
        regex=r"[\d\(\)\-\s\+]+",
        label="Phone Number",
        max_length=20,
        help_text="Phone must consist only digits spaces or + ( ) -",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter phone number",
                "class": "form-control",
                "pattern": "^[0-9\+\-\(\)\s]{8,20}$"
                }))

    def clean(self):
        if self.is_valid():
            phone = sub(r"[^\d\+]", "",self.cleaned_data['phone'])
            if phone.startswith("04") and len(phone) == 10:
                self.cleaned_data['phone'] = f"{phone[:4]} {phone[4:7]} {phone[7:]}"
            elif phone.startswith('+') and len(phone) == 11:
                self.cleaned_data['phone'] = f"+{phone[1:3]} {phone[3]} {phone[4:8]} {phone[8:]}"
            elif phone[:2] in ["02", "03", "07", "08"] and len(phone) == 10:
                self.cleaned_data['phone'] = f"({phone[:2]}) {phone[2:6]} {phone[6:]}"

