# Generated by Django 3.2.9 on 2021-12-08 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0005_rename_liked_by_save_saved_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='saved_by',
        ),
    ]
