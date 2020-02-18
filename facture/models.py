from django.db import models
from devis.models import Devis


class Facture(models.Model):

    devis = models.OneToOneField(Devis, on_delete=models.CASCADE)
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

class LineFacture(models.Model):

    description = models.CharField(max_length=100)
    qte = models.IntegerField()
    puht = models.FloatField()
    line = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='linefacture')
    
    def sub_total(self):
        return self.qte * self.puht

