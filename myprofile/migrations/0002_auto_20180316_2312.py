# Generated by Django 2.0.2 on 2018-03-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
