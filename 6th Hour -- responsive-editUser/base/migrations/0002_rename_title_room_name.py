# Generated by Django 3.2 on 2022-01-19 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='title',
            new_name='name',
        ),
    ]
