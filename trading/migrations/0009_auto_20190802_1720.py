# Generated by Django 2.2 on 2019-08-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0008_historicalprices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprices',
            name='change',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='changeOverTime',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='changePercent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='high_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='low_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='open_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='uClose',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='uHigh',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='uLow',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='uOpen',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='uVolume',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprices',
            name='volume',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]