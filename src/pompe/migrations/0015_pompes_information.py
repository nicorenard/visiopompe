# Generated by Django 3.2.6 on 2021-09-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pompe', '0014_auto_20210909_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='pompes',
            name='information',
            field=models.CharField(default='', max_length=200),
        ),
    ]
