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


class HomePageView(TemplateView):

    model = Client
    template_name = 'facturier/home.html'


class ClientCreateView(CreateView):

    model = Client
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["address_client"] = AddressInlineFormSet(instance=self.get_object())
        return context

class ClientListView(ListView):

    model = Client

class ClientDetailView(DetailView):

    model = Client

class ClientUpdateView(UpdateView):

    model = Client
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('detail-client', args = [self.object.id])

    
class ClientDeleteView(DeleteView):

    model = Client
    success_url = reverse_lazy('list-client')

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)

# class AdressView(AdressView):

#     model = Client, Adress
