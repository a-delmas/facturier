# Generated by Django 3.0.3 on 2020-02-20 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0002_facture_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
