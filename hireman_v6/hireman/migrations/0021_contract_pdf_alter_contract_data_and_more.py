# Generated by Django 4.1.7 on 2023-08-04 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireman', '0020_alter_contract_data_alter_reparatie_data_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='pdf',
            field=models.ImageField(default='hireman/static/contracte_pdf/contract-nr<django.db.models.fields.IntegerField>-din:<django.db.models.fields.DateField>', null=True, upload_to='hireman/static/contracte_pdf/'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 14, 40, 54, 167515, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_end',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 14, 40, 54, 167515, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_start',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 14, 40, 54, 167515, tzinfo=datetime.timezone.utc)),
        ),
    ]
