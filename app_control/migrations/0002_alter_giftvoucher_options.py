# Generated by Django 5.0.2 on 2024-03-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='giftvoucher',
            options={'ordering': ['created_at']},
        ),
    ]
