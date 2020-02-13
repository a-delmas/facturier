from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "raison_sociale"]

admin.site.register(Client, ClientAdmin)
