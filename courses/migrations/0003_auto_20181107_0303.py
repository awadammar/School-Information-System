# Generated by Django 2.1.2 on 2018-11-07 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181104_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
