# Generated by Django 3.0.2 on 2020-01-11 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myTickets', '0003_auto_20200111_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='year_of_birth',
        ),
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
