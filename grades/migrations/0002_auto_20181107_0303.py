# Generated by Django 2.1.2 on 2018-11-07 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='examine_at',
            field=models.DateField(default=datetime.datetime(2018, 11, 7, 3, 3, 38, 228095)),
        ),
        migrations.AlterField(
            model_name='grade',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]