from django.contrib import admin
from .models import Devis

# Register your models here.


class DevisAdmin(admin.ModelAdmin):

    model = Devis

    list_display = ['date']

admin.site.register(Devis, DevisAdmin)