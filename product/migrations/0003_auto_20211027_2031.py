# Generated by Django 3.2.7 on 2021-10-27 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211027_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first',
            new_name='SeName',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last',
        ),
    ]
