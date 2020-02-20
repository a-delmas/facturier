from django.forms import inlineformset_factory
from .models import Facture, LineFacture, Devis
from django import forms

LineInlineFormSet = inlineformset_factory(Facture, LineFacture, 
                                            fields = '__all__',
                                            exclude = ([]),
                                            can_delete = True, 
                                            extra = 1
)

TransformDevisFormSet = inlineformset_factory(Devis, Facture,
                                                fields = '__all__',
                                                can_delete = True,
                                                
)

