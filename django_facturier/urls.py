"""django_facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from facturier.views import HomePageView, ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView
from devis.views import DevisListView, DevisDetailView, DevisCreateView, DevisUpdateView, DevisDeleteView, DevisPrintView
from facture.views import FactureListView, FactureDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('register/', ClientCreateView.as_view(), name='register'),
    path('clients/', ClientListView.as_view(), name='list-client'),
    path('clients/<int:pk>/detail', ClientDetailView.as_view(), name='detail-client'),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name="update-client"),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name="delete-client"),
    path('devis/detail', DevisListView.as_view(), name='list-devis'),
    path('devis/<int:pk>/detail', DevisDetailView.as_view(), name='detail-devis'),
    path('devis/new', DevisCreateView.as_view(), name='create-devis'),
    path('devis/<int:pk>/update', DevisUpdateView.as_view(), name='update-devis'),
    path('devis/<int:pk>/delete', DevisDeleteView.as_view(), name='delete-devis'),
    path('generate/<int:pk>/pdf', DevisPrintView.as_view(), name='generate_pdf'),
    path('facture/', FactureListView.as_view(), name='list-facture'),
    path('facture/<int:pk>/detail', FactureDetailView.as_view(), name='detail-facture'),
   
    # path('adresss/',AdressView )
]
