# Generated by Django 4.0.6 on 2022-07-24 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SYSControl', '0003_remove_database_user_profile_database_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]