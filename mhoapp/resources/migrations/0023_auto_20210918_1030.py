# Generated by Django 3.1.7 on 2021-09-18 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0022_auto_20210918_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resourcepage',
            old_name='leftColumn',
            new_name='left_column',
        ),
        migrations.RenameField(
            model_name='resourcepage',
            old_name='rightColumn',
            new_name='right_column',
        ),
        migrations.RenameField(
            model_name='resourcesindexpage',
            old_name='leftColumn',
            new_name='left_column',
        ),
        migrations.RenameField(
            model_name='resourcesindexpage',
            old_name='rightColumn',
            new_name='right_column',
        ),
    ]