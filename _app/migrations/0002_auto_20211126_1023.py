# Generated by Django 3.0 on 2021-11-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paket_tour',
            name='list_paket',
        ),
        migrations.AddField(
            model_name='paket_tour',
            name='list_paket',
            field=models.ManyToManyField(to='_app.List_tour'),
        ),
    ]
