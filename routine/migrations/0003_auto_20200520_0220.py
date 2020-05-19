# Generated by Django 2.2.6 on 2020-05-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0002_auto_20200518_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routine',
            old_name='solt',
            new_name='slot',
        ),
        migrations.AlterField(
            model_name='routine',
            name='day',
            field=models.CharField(choices=[('saturday', 'Saturday'), ('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('extra', 'Extra')], max_length=12),
        ),
    ]
