from django.db import models

# Create your models here.

class Client(models.Model):

    def __str__(self):
        return self.raison_sociale

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel = models.IntegerField()
    raison_sociale = models.CharField(max_length=100)
    siret = models.IntegerField()
    tva = models.CharField(max_length=13)
    email = models.CharField(max_length=50)

class Address(models.Model):

    ADDRESS_CHOICES =[
        ('SH', 'Livraison'),
        ('BL', 'Facturation'),
        ('HQ', 'Siège Social'),
    ]
    addressType = models.CharField(max_length=15, choices=ADDRESS_CHOICES, blank=True)

    num = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    complement = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)