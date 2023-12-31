# Generated by Django 4.2.5 on 2023-09-21 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireman', '0024_alter_contract_adresa_livrare_alter_contract_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 0, 51, 26, 356991, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='pdf_path',
            field=models.FileField(default='hireman/static/contracte_pdf/contract-nr1-din:2023-09-21 00:51:26.356991+00:00', null=True, upload_to='hireman/static/contracte_pdf/'),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_end',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 0, 51, 26, 354980, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_start',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 0, 51, 26, 354980, tzinfo=datetime.timezone.utc)),
        ),
    ]
