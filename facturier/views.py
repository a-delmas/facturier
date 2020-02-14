from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, ModelFormMixin
from django.views.generic import TemplateView
from .models import Client, Address
from django.contrib.auth.forms import UserCreationForm
from facturier.forms import AddressInlineFormSet
from django.http import HttpResponseRedirect, HttpResponse
from django import forms



class HomePageView(TemplateView):

    model = Client
    template_name = 'facturier/home.html'


class ClientCreateView(CreateView):

    model = Client
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["address_client"] = AddressInlineFormSet()
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        if form.is_valid():
            self.object = form.save(commit=False)
            address_form = AddressInlineFormSet(self.request.POST, self.request.FILES, instance = self.object)
            if address_form.is_valid():
                form.save()
                # form.save_m2m()
                address_form.save()
                # login(self.request, self.object)
                return HttpResponseRedirect(self.get_success_url())
    
        context = {
            'form' : form,
            'address_form' : address_form
        }
        return self.render_to_response(context)


class ClientListView(ListView):

    model = Client



class ClientDetailView(DetailView):

    model = Client



class ClientUpdateView(UpdateView):

    model = Client
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('detail-client', args = [self.object.id])

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["address_client"] = AddressInlineFormSet()
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        address_form = AddressInlineFormSet(self.request.POST)
        if form.is_valid() and address_form.is_valid():
            form.save()
            address_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = {
                'form' : form,
                'address_form' : address_form
            }
            return self.render_to_response(context)


    
class ClientDeleteView(DeleteView):

    model = Client
    success_url = reverse_lazy('list-client')

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)

# class AdressView(AdressView):

#     model = Client, Adress
