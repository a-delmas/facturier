from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, ModelFormMixin
from django.views.generic import TemplateView
from .models import Client
from django.contrib.auth.forms import UserCreationForm


class HomePageView(TemplateView):

    model = Client
    template_name = 'facturier/home.html'


class ClientCreateView(CreateView):

    model = Client
    # form_class = UserCreationForm
    fields = '__all__'
    success_url = '/'

class ClientListView(ListView):

    model = Client

class ClientDetailView(DetailView):

    model = Client

class ClientUpdateView(UpdateView):

    model = Client
    form_class = ClientCreateView
    template_name = 'facturier/client_form.html'

    