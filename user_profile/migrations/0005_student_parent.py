# Generated by Django 3.2 on 2024-04-30 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_remove_parent_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profile.parent'),
        ),
    ]