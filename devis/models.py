from django.db import models
from django.db.models import Sum
from facturier.models import Client

# Create your models here.

class Devis(models.Model):

    client_devis = models.ForeignKey(Client, on_delete=models.CASCADE)
    # address_devis = models.ManyToManyField(Address, on_delete=models.CASCADE)
    date = models.DateField()

    def total_ht(self):
        result = 0
        for totht in self.linedevis.all():
            result += totht.sub_total()
        return result        

    def total_tva(self):
        result = 0
        result = self.total_ht() * (20/100)
        return result    

    def total_ttc(self):
        result = self.total_ht() * (1+(20/100))
        return result

class LineDevis(models.Model):

    description = models.CharField(max_length=100)
    qte = models.IntegerField()
    puht = models.FloatField()
    line = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name='linedevis')
    
    def sub_total(self):
        return self.qte * self.puht
