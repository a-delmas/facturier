from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, ModelFormMixin
from django.views.generic import TemplateView
from .models import Devis, LineDevis, Client
from facture.models import Facture, LineFacture
from facturier.models import Address
from django.contrib.auth.forms import UserCreationForm
from .forms import LineInlineFormSet
from django.http import HttpResponseRedirect, HttpResponse
from django import forms

from django.conf import settings

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG

class DevisListView(ListView):

    model = Devis

    template_name = 'devis_list.html'


class DevisDetailView(DetailView):

    model = Devis

    template_name = 'devis_detail.html'
    success_url = reverse_lazy('facture.html')

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["address_choice"] = self.get_object().client_devis.address_set.filter(addressType='BL').first()
        return context



class DevisPrintView(WeasyTemplateResponseMixin, DevisDetailView):

    pdf_attachment = True
    pdf_filename = 'devis.pdf'

    def get_context_data(self, **kwargs):
        context = DevisDetailView.get_context_data(self, **kwargs)
        context['pdf'] = True
        return context
    
    def get_pdf_filename(self):
        return 'devis{}.pdf'.format(self.get_object().id)
        


class DevisCreateView(CreateView):

    model = Devis
    fields = '__all__'

    template_name = 'devis_create.html'

    def get_success_url(self):
        return reverse_lazy('detail-devis', args = [self.object.id])

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["devis_line"] = LineInlineFormSet()
        return context

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            devis_line = LineInlineFormSet(self.request.POST, self.request.FILES, instance = self.object)
            if devis_line.is_valid():
                form.save()
                devis_line.save()
                # login(self.request, self.object)
                return HttpResponseRedirect(self.get_success_url())
    
        context = {
            'form' : form,
            'devis_line' : devis_line
        }
        return self.render_to_response(context)


class DevisUpdateView(UpdateView):

    model = Devis
    fields = '__all__'
    template_name = 'devis_create.html'

    def get_success_url(self):
        return reverse_lazy('detail-devis', args = [self.object.id])

    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context["devis_line"] = LineInlineFormSet(instance=self.get_object())
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        devis_line = LineInlineFormSet(self.request.POST, instance = self.object)
        if form.is_valid() and devis_line.is_valid():
            form.save()
            devis_line.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = {
                'form' : form,
                'devis_line' : devis_line
            }
            return self.render_to_response(context)



class DevisDeleteView(DeleteView):

    model = Devis
    success_url = reverse_lazy('list-devis')


class TransformDevisToFactureView(DetailView):

    model = Devis
    template_name = "facture.html"




