# Generated by Django 4.0.3 on 2022-03-17 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0004_detailsmodel_drivercommision'),
        ('JobDetails', '0006_alter_jobmodels_jobrefered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodels',
            name='jobrefered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Driver.detailsmodel'),
        ),
    ]
