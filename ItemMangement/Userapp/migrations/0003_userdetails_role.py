# Generated by Django 4.0.3 on 2022-03-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0002_alter_userdetails_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='role',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
