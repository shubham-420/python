# Generated by Django 3.0.5 on 2020-04-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='ans',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]