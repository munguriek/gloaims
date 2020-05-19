# Generated by Django 2.2.6 on 2020-05-11 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acade_owner', '0033_auto_20200511_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='rent_from',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rent',
            name='rent_to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]