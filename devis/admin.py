from django.contrib import admin
from devis.models import Devis, LineDevis

# Register your models here.

class LineDevisAdmin(admin.TabularInline):

    model = LineDevis


class DevisAdmin(admin.ModelAdmin):

    inlines = [LineDevisAdmin]
    list_display = ['date']

admin.site.register(Devis, DevisAdmin)