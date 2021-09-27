# Generated by Django 3.2.6 on 2021-08-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pompe', '0003_auto_20210825_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Huile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='pompes',
            name='localisation',
        ),
        migrations.RemoveField(
            model_name='pompes',
            name='position',
        ),
        migrations.AddField(
            model_name='piecespompe',
            name='localisation',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='pompes',
            name='localisation_emplacement',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pompes',
            name='localisation_etage',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='pompes',
            name='localisation_piece',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='pompes',
            name='code_umr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pompes',
            name='marque',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pompes',
            name='nom',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pompes',
            name='numero_serie',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pompes',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
