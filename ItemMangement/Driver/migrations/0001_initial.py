# Generated by Django 4.0.3 on 2022-03-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docimage', models.ImageField(upload_to='Documents')),
            ],
        ),
        migrations.CreateModel(
            name='DetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prof_image', models.ImageField(upload_to='ProfileImage')),
                ('Phone', models.CharField(max_length=100)),
                ('documents', models.ManyToManyField(to='Driver.documentsmodel')),
            ],
        ),
    ]