# Generated by Django 3.0.3 on 2020-04-07 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200407_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='confirmed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='referral',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
    ]
