# Generated by Django 4.0.3 on 2022-03-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobDetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodels',
            name='drivercommision',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='jobmodels',
            name='referercommision',
            field=models.CharField(default=0, max_length=100),
        ),
    ]