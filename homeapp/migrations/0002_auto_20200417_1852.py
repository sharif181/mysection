# Generated by Django 2.2.6 on 2020-04-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='time',
            field=models.TimeField(),
        ),
    ]