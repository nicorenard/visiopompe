# Generated by Django 3.2.6 on 2021-08-25 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pompe', '0002_pompe_nombre_etage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PiecePompe',
            new_name='PiecesPompe',
        ),
        migrations.RenameModel(
            old_name='Pompe',
            new_name='Pompes',
        ),
    ]
