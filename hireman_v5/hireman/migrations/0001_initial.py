# Generated by Django 4.1.7 on 2023-05-07 16:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Categori',
                'verbose_name_plural': 'Categorii',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('cnp', models.IntegerField(null=True)),
                ('adresa', models.CharField(max_length=150)),
                ('tel', models.IntegerField()),
                ('mail', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clienti',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Cos',
                'verbose_name_plural': 'Cosuri',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PretProdus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pret_1', models.IntegerField()),
                ('pret_2', models.IntegerField()),
                ('pret_3', models.IntegerField()),
                ('pret_4', models.IntegerField()),
                ('pret_5', models.IntegerField()),
                ('pret_w', models.IntegerField()),
                ('pret_s', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Pret',
                'verbose_name_plural': 'Preturi',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('cod_produs', models.IntegerField()),
                ('descriere', models.TextField()),
                ('specificatii', models.TextField()),
                ('status', models.CharField(choices=[('disponibil', 'disponibil'), ('nedisponibil', 'nedisponibil'), ('service', 'service')], default='disponibil', max_length=20)),
                ('poza', models.ImageField(null=True, upload_to='media/')),
                ('garantie', models.IntegerField(default=600)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hireman.categorie')),
                ('pret', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hireman.pretprodus')),
            ],
            options={
                'verbose_name': 'Produs',
                'verbose_name_plural': 'Produse',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Societate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('ro', models.IntegerField()),
                ('cui', models.IntegerField()),
                ('adresa', models.CharField(max_length=150)),
                ('director', models.CharField(max_length=50)),
                ('tel', models.BigIntegerField()),
                ('mail', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Societate',
                'verbose_name_plural': 'Societati',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reparatie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_service', models.CharField(max_length=50)),
                ('tel', models.IntegerField()),
                ('mail', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('data_start', models.DateField(verbose_name=datetime.datetime(2023, 5, 7, 19, 35, 11, 133217))),
                ('data_end', models.DateField(verbose_name=datetime.datetime(2023, 5, 7, 19, 35, 11, 133217))),
                ('produs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hireman.produs')),
            ],
            options={
                'verbose_name': 'Reparatie',
                'verbose_name_plural': 'Reparatii',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Recenzie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=5, max_length=2)),
                ('coment', models.TextField()),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hireman.produs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hireman.client')),
            ],
            options={
                'verbose_name': 'Recenzie',
                'verbose_name_plural': 'Recenzii',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nr', models.IntegerField()),
                ('data', models.DateField(default=datetime.date(2023, 5, 7))),
                ('perioada', models.CharField(choices=[('1', '1 zi'), ('2', '2 zile'), ('3', '3 zile'), ('4', '4 zile'), ('5', '5 zile'), ('w', 'weekend'), ('s', 'o saptamana')], default=1, max_length=50)),
                ('data_start', models.DateTimeField(auto_now_add=True)),
                ('data_end', models.DateTimeField()),
                ('observatii', models.CharField(max_length=255, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hireman.client')),
                ('societate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hireman.societate')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='cos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hireman.cos'),
        ),
    ]
