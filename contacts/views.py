from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Contact
from .forms import ContactDetailsForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class ContactsView(LoginRequiredMixin, ListView):
    template_name = "listing.html"
    model = Contact
    context_object_name = "listing"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = self.queryset
        context['search_bar'] = True
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class AddContactView(CreateView, LoginRequiredMixin):
    template_name = "add_modify.html"
    form_class = ContactDetailsForm
    success_url = reverse_lazy("listing")
    model = Contact
    extra_context = {
        "heading": "Add contact",
        "button": 'Add',
        "action": reverse_lazy('add'),
        "active": 2,
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(get_random_string(length=16))
        self.object = form.save()
        messages.success(self.request, "Contact added successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Contacts form was invalid")
        return redirect('listing')


class ModifyContactView(UpdateView, LoginRequiredMixin):
    template_name = "add_modify.html"
    success_url = reverse_lazy("listing")
    model = Contact
    form_class = ContactDetailsForm
    extra_context = {
        "heading": "Update contact",
        "button": "Update"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse_lazy('modify', kwargs={"slug": self.object.slug})
        return context

    def form_valid(self, form):
        if self.object.owner == self.request.user:
            self.object.save()
            messages.success(self.request, "Contact updated successfully.")
        else:
            messages.error(self.request, "Contact not modified.")
        return redirect('listing')


class DeleteContactView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Contact
    success_url = reverse_lazy('listing')

    def form_valid(self, form):
        if self.object.owner == self.request.user:
            self.object.delete()
            messages.success(self.request, "Contact deleted successfully.")
        else:
            messages.error(self.request, "Contact not deleted")
        return redirect(self.success_url)
