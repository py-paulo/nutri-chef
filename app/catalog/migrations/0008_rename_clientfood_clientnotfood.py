# Generated by Django 4.2 on 2023-04-29 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_created_at_client_updated_at'),
        ('catalog', '0007_clientfood'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientFood',
            new_name='ClientNotFood',
        ),
    ]