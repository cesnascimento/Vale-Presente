# Generated by Django 5.0.2 on 2024-03-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0003_alter_store_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftvoucher',
            name='status_bar_code',
        ),
        migrations.AddField(
            model_name='barcode',
            name='status_bar_code',
            field=models.BooleanField(default=False),
        ),
    ]