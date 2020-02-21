from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, ModelFormMixin
from django.views.generic import TemplateView
from devis.models import Devis, LineDevis
from facture.models import Facture, LineFacture
from facturier.models import Address, Client
from django.contrib.auth.forms import UserCreationForm
from .forms import LineInlineFormSet
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.conf import settings

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG

class FactureListView(ListView):

    model = Facture

    template_name = 'facture_list.html'


class FactureDetailView(PermissionRequiredMixin, DetailView):

    model = Facture

    template_name = 'facture_detail.html'
    permission_required = ('facture.view_facture')

    # def get_context_data(self, **kwargs):
    #     context = DetailView.get_context_data(self, **kwargs)
    #     context["consult_facture"] = LineInlineFormSet(instance=self.get_object())
    #     return context


class FacturePrintView(WeasyTemplateResponseMixin, FactureDetailView):

    pdf_attachment = True
    pdf_filename = 'facture.pdf'

    def get_context_data(self, **kwargs):
        context = FactureDetailView.get_context_data(self, **kwargs)
        context['pdf'] = True
        return context
    
    def get_pdf_filename(self):
        return 'facture{}.pdf'.format(self.get_object().id)



