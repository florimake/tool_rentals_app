# Generated by Django 4.1.7 on 2023-08-01 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireman', '0019_contract_cost_contract_garantie_produs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 8, 1, 13, 22, 30, 4709, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_start',
            field=models.DateField(default=datetime.datetime(2023, 8, 1, 13, 22, 30, 4709, tzinfo=datetime.timezone.utc)),
        ),
    ]
