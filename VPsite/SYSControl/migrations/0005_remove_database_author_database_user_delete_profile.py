# Generated by Django 4.0.6 on 2022-07-25 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SYSControl', '0004_remove_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='database',
            name='author',
        ),
        migrations.AddField(
            model_name='database',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
