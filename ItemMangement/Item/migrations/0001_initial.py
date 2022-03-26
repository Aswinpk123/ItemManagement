# Generated by Django 4.0.3 on 2022-03-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemname', models.CharField(max_length=100)),
                ('Itemdesc', models.CharField(max_length=100)),
                ('Created_Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Typename', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('Created_Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
