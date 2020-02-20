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
# from .forms import LineInlineFormSet
from django.http import HttpResponseRedirect, HttpResponse
from django import forms

from django.conf import settings

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG

class FactureListView(ListView):

    model = Facture

    template_name = 'facture_list.html'


class FactureDetailView(DetailView):

    model = Facture

    template_name = 'facture_detail.html'

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["consult_facture"] = self.get_object()
        return context



# class FacturePrintView(WeasyTemplateResponseMixin, FactureDetailView):

#     pdf_attachment = True
#     pdf_filename = 'Facture.pdf'

#     def get_context_data(self, **kwargs):
#         context = FactureDetailView.get_context_data(self, **kwargs)
#         context['pdf'] = True
#         return context
    
#     def get_pdf_filename(self):
#         return 'Facture{}.pdf'.format(self.get_object().id)
        


# class FactureCreateView(CreateView):

#     model = Facture
#     fields = '__all__'

#     template_name = 'Facture_create.html'

#     def get_success_url(self):
#         return reverse_lazy('detail-Facture', args = [self.object.id])

#     def get_context_data(self, **kwargs):
#         context = CreateView.get_context_data(self, **kwargs)
#         context["Facture_line"] = LineInlineFormSet()
#         return context

#     def form_valid(self, form):
#         if form.is_valid():
#             self.object = form.save(commit=False)
#             Facture_line = LineInlineFormSet(self.request.POST, self.request.FILES, instance = self.object)
#             if Facture_line.is_valid():
#                 form.save()
#                 Facture_line.save()
#                 # login(self.request, self.object)
#                 return HttpResponseRedirect(self.get_success_url())
    
#         context = {
#             'form' : form,
#             'Facture_line' : Facture_line
#         }
#         return self.render_to_response(context)


# class FactureUpdateView(UpdateView):

#     model = Facture
#     fields = '__all__'
#     template_name = 'Facture_create.html'

#     def get_success_url(self):
#         return reverse_lazy('detail-Facture', args = [self.object.id])

#     def get_context_data(self, **kwargs):
#         context = UpdateView.get_context_data(self, **kwargs)
#         context["Facture_line"] = LineInlineFormSet(instance=self.get_object())
#         return context

#     def form_valid(self, form):
#         """If the form is valid, save the associated model."""
#         Facture_line = LineInlineFormSet(self.request.POST, instance = self.object)
#         if form.is_valid() and Facture_line.is_valid():
#             form.save()
#             Facture_line.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             context = {
#                 'form' : form,
#                 'Facture_line' : Facture_line
#             }
#             return self.render_to_response(context)



# class FactureDeleteView(DeleteView):

#     model = Facture
#     success_url = reverse_lazy('list-Facture')