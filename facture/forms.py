from django.forms import inlineformset_factory
from .models import Facture, LineFacture
from django import forms

LineInlineFormSet = inlineformset_factory(Facture, LineFacture, 
                                            fields = '__all__',
                                            exclude = ([]),
                                            can_delete = True, 
                                            extra = 1
)

