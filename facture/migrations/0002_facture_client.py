# Generated by Django 3.0.3 on 2020-02-20 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0004_auto_20200213_1524'),
        ('facture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturier.Client'),
        ),
    ]
