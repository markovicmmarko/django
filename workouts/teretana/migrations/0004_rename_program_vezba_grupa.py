# Generated by Django 5.0.4 on 2024-05-21 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teretana', '0003_vezba'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vezba',
            old_name='program',
            new_name='grupa',
        ),
    ]
