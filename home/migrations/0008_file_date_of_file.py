# Generated by Django 3.0.5 on 2020-08-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_file_date_of_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='date_of_file',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]