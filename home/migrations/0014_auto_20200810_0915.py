# Generated by Django 3.0.5 on 2020-08-10 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200810_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='moved_to_perm_sec2',
            new_name='moved_by_perm_sec2',
        ),
    ]