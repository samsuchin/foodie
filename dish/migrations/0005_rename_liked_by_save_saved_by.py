# Generated by Django 3.2.9 on 2021-12-06 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0004_save'),
    ]

    operations = [
        migrations.RenameField(
            model_name='save',
            old_name='liked_by',
            new_name='saved_by',
        ),
    ]
