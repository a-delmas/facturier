from django.forms import inlineformset_factory
from .models import Devis, LineDevis
from django import forms

LineInlineFormSet = inlineformset_factory(Devis, LineDevis, 
                                            fields = '__all__',
                                            exclude = ([]),
                                            can_delete = True, 
                                            )

# AddressChoices(forms.Form):
    # choice_fields = forms.ChoiceField(choice = ADDRESS_CHOICES)