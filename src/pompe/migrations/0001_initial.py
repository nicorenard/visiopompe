# Generated by Django 3.2.6 on 2021-08-25 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PiecePompe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('image', models.ImageField(max_length=500, upload_to='')),
                ('marque', models.CharField(max_length=50)),
                ('type_pompe', models.CharField(max_length=100)),
                ('quantite', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pompe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=500, upload_to='')),
                ('nom', models.CharField(max_length=100)),
                ('marque', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=300)),
                ('puissance', models.FloatField(default=0)),
                ('code_umr', models.CharField(max_length=300)),
                ('localisation', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=300)),
                ('mise_en_service', models.DateField(default=datetime.date.today)),
                ('statut', models.CharField(choices=[('A', 'Active'), ('S', 'Stockage'), ('R', 'En Réparation'), ('EP', 'En panne'), ('HS', 'Hors Service')], default='A', max_length=2)),
                ('date_derniere_vidange', models.DateField(auto_now=True)),
                ('huile', models.CharField(max_length=50)),
                ('kit_maintenance', models.BooleanField(default=False)),
            ],
        ),
    ]
