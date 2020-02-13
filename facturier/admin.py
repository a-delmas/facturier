from django.contrib import admin
from .models import Client, Address


class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "raison_sociale"]

admin.site.register(Client, ClientAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ["address"]

admin.site.register(Address, AddressAdmin)