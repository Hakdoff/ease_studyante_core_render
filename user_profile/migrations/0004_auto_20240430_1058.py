# Generated by Django 3.2 on 2024-04-30 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20240410_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profile.parent'),
        ),
    ]