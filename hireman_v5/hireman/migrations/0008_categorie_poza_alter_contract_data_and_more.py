# Generated by Django 4.1.7 on 2023-06-28 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireman', '0007_alter_contract_data_alter_contract_data_start_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='poza',
            field=models.ImageField(null=True, upload_to='media/category'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='data',
            field=models.DateField(default=datetime.date(2023, 6, 28)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='data_start',
            field=models.DateField(default=datetime.date(2023, 6, 28)),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_end',
            field=models.DateField(default=datetime.date(2023, 6, 28)),
        ),
        migrations.AlterField(
            model_name='reparatie',
            name='data_start',
            field=models.DateField(default=datetime.date(2023, 6, 28)),
        ),
    ]
