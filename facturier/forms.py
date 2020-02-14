from django.forms import inlineformset_factory
from .models import Client, Address
from django import forms


AddressInlineFormSet = inlineformset_factory(Client, Address, 
                                                fields = '__all__',
                                                exclude = ([]),
                                                can_delete = True,
                                                max_num = 5,
                                                extra = 5

)