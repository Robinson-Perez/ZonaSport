# Generated by Django 3.2.8 on 2021-10-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='pago',
            field=models.CharField(choices=[('Total', 'Cancelado'), ('Anticipo', 'Anticipo')], default='', max_length=20),
        ),
    ]
