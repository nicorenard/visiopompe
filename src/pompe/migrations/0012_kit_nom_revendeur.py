# Generated by Django 3.2.6 on 2021-09-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pompe', '0011_auto_20210909_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='kit',
            name='nom_revendeur',
            field=models.CharField(default='', max_length=40),
        ),
    ]