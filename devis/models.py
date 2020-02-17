from django.db import models
from facturier.models import Client

# Create your models here.

class Devis(models.Model):

    client_devis = models.ForeignKey(Client, on_delete=models.CASCADE)
    # address_devis = models.ManyToManyField(Address, on_delete=models.CASCADE)
    date = models.DateField()

class LineDevis(models.Model):

    description = models.CharField(max_length=100)
    qte = models.IntegerField()
    puht = models.FloatField()
    line = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name='linedevis')
    
    def sub_total(self):
        return self.qte * self.puht