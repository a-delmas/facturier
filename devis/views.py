from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, ModelFormMixin
from django.views.generic import TemplateView
from .models import Devis, LineDevis, Client
from facturier.models import Address
from django.contrib.auth.forms import UserCreationForm
from .forms import LineInlineFormSet
from django.http import HttpResponseRedirect, HttpResponse
from django import forms



class DevisListView(ListView):

    model = Devis

    template_name = 'devis_list.html'

class DevisDetailView(DetailView):

    model = Devis

    # form = AddressChoices

    template_name = 'devis_detail.html'

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["address_choice"] = self.get_object().client_devis.address_set.filter(addressType='BL').first()
        return context

    # def AddressChoices(request):
    #     choice = Address.objects.filter.all()
    #     return object_list(request, template_name = 'devis_detail.html', querySet= choice)