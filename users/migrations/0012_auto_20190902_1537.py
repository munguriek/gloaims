# Generated by Django 2.2.3 on 2019-09-02 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='users.Status'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
