# Generated by Django 3.2 on 2024-03-13 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='year_level',
        ),
    ]