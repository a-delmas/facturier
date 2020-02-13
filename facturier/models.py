from django.db import models

# Create your models here.

class Client(models.Model):

    def __str__(self):
        return self.raison_sociale

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel = models.IntegerField(max_length=10)
    raison_sociale = models.CharField(max_length=100)
    siret = models.IntegerField(max_length=14)
    tva = models.CharField(max_length=13)
    email = models.CharField(max_length=50)

class Address(models.Model):
    num = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    complement = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(max_length=5, null=True)
    town = models.CharField(max_length=50, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)