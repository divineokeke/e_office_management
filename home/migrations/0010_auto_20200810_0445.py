# Generated by Django 3.0.5 on 2020-08-10 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_file_file_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='moved_by_perm_sec1',
            new_name='moved_to_perm_sec1',
        ),
    ]
