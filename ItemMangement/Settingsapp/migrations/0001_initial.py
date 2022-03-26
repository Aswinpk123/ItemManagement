# Generated by Django 4.0.3 on 2022-03-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perkmcharge', models.CharField(max_length=100)),
                ('extracharge', models.CharField(max_length=100)),
                ('extradescription', models.CharField(max_length=100)),
                ('referorcommision', models.CharField(max_length=100)),
                ('drivercommision', models.CharField(max_length=100)),
                ('keyvalue', models.CharField(default=1, max_length=100)),
            ],
        ),
    ]
