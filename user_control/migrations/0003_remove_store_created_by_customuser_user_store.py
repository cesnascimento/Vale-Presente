# Generated by Django 5.0.2 on 2024-03-14 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0002_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='created_by',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user_control.store'),
        ),
    ]
