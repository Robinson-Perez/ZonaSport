# Generated by Django 3.2.8 on 2021-10-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_reservas_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='monto',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
