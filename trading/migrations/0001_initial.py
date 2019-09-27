# Generated by Django 2.2 on 2019-07-26 15:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbols',
            fields=[
                ('symbol', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('isEnabled', models.BooleanField(default=True)),
                ('symbol_type', models.CharField(choices=[('ADR', 'ADR'), ('REIT', 'REIT'), ('Closed end fund', 'Closed end fund'), ('Secondary Issue', 'Secondary Issue'), ('Limited Partnerships', 'Limited Partnerships'), ('Common Stock', 'Common Stock'), ('ETF', 'ETF')], max_length=10)),
                ('iexId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WatchSymbols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enter', models.DateField(default=datetime.date.today)),
                ('notes', models.TextField(max_length=200)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.Symbols')),
            ],
        ),
    ]