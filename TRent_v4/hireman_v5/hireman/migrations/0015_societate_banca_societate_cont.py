# Generated by Django 4.1.7 on 2023-08-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireman', '0014_remove_societate_banca_remove_societate_cont'),
    ]

    operations = [
        migrations.AddField(
            model_name='societate',
            name='banca',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='societate',
            name='cont',
            field=models.IntegerField(null=True),
        ),
    ]
