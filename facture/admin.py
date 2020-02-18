from django.contrib import admin
from facture.models import Facture, LineFacture
# Register your models here.

class LineFactureAdmin(admin.TabularInline):

    model = LineFacture


class FactureAdmin(admin.ModelAdmin):

    inlines = [LineFactureAdmin]
    list_display = ['date']

admin.site.register(Facture, FactureAdmin)