from django.contrib import admin
from facturier.models import Client, Address

class AddressAdmin(admin.TabularInline):

    model = Address
    
    list_display = ["address"]

# admin.site.register(Address, AddressAdmin)

class ClientAdmin(admin.ModelAdmin):

    inlines = [AddressAdmin]

    list_display = ["first_name", "last_name", "raison_sociale"]

admin.site.register(Client, ClientAdmin)