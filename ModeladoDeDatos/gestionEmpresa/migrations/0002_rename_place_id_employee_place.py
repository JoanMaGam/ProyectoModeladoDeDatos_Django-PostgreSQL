# Generated by Django 4.1.5 on 2023-03-05 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEmpresa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='place_id',
            new_name='place',
        ),
    ]
