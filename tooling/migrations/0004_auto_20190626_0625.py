# Generated by Django 2.2 on 2019-06-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tooling', '0003_auto_20190529_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='photo',
            field=models.ImageField(blank=True, upload_to='tool/'),
        ),
    ]
