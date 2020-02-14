from django.forms import inlineformset_factory
from .models import Client, Address
from django import forms


AddressInlineFormSet = inlineformset_factory(Client, Address, fields= ['addressType', 'num', 'address', 'complement', 'zipcode', 'town'])