# Generated by Django 3.0.5 on 2020-07-21 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200721_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='titleman',
            new_name='title',
        ),
    ]
