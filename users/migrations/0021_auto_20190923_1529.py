# Generated by Django 2.2.3 on 2019-09-23 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acade_owner', '0012_auto_20190923_1529'),
        ('users', '0020_book_date_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='approve_comment',
            field=models.CharField(max_length=1000, verbose_name='Add a comment'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='users.BookStatus', verbose_name='Booking Status'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('user', 'room')},
        ),
    ]
