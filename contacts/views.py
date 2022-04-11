from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Contact
from .forms import ContactDetailsForm, RegisterUserForm, SearchContactsForm 
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

def home_page(request):
    return render(request, "home.html")

@login_required(login_url="/auth/login")
def contacts_page(request):
    if request.method == "POST":
        form = SearchContactsForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            contacts =\
                Contact.objects.filter(
                    (Q(firstname__icontains=query) |\
                    Q(lastname__icontains=query) |\
                    Q(email__icontains=query) |\
                    Q(phone=query)) &\
                    Q(owner=request.user)
                )
    else:
        contacts = Contact.objects.filter(owner=request.user)
    context = {
        "active": 1,
        "contacts": contacts,
        "search_form": SearchContactsForm(),
    }
    return render(request, "contacts.html", context)


class AddContactView(CreateView, LoginRequiredMixin):
    template_name = "add_modify.html"
    form_class = ContactDetailsForm
    success_url = reverse_lazy("contacts")
    model = Contact
    extra_context = {
        "heading": "Add contact",
        "action": reverse_lazy('add'),
        "active": 2,
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Contact added successfully.")
        return super().form_valid(form)


class UpdateContactView(UpdateView, LoginRequiredMixin):
    template_name = "add_modify.html"
    success_url = reverse_lazy("contacts")
    model = Contact
    form_class = ContactDetailsForm
    extra_context = {
        "heading": "Update contact",
        "action": reverse_lazy('update'),
    }

    def form_valid(self, form):
        messages.success(self.request, "Contact updated successfully.")
        return super().form_valid(form)

class DeleteContactView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Contact
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        if self.object.owner == self.request.user:
            self.object.delete()
            messages.success(self.request, "Contact deleted successfully.")
        else:
            messages.error(self.request, "Contact not deleted")
        return redirect(self.success_url)


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "User Registered Successfully")
            return redirect("contacts")
        messages.error(request, "Registration Failed")

    context = {
        "registration_form": RegisterUserForm()
    }
    return render(request, "register.html", context)
