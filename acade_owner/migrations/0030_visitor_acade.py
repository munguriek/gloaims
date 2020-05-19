# Generated by Django 2.2.3 on 2019-09-27 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acade_owner', '0029_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='acade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acade_owner.Acade', verbose_name='Building'),
        ),
    ]