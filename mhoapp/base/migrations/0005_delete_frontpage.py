# Generated by Django 3.1.7 on 2021-03-01 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('base', '0004_auto_20210226_2029'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FrontPage',
        ),
    ]