# Generated by Django 2.2.3 on 2019-09-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20190925_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]