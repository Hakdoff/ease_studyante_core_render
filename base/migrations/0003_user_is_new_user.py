# Generated by Django 3.2 on 2024-04-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20240306_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_new_user',
            field=models.BooleanField(default=True),
        ),
    ]
