# Generated by Django 3.1.7 on 2021-02-24 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerpage',
            name='types',
        ),
        migrations.DeleteModel(
            name='TypeCategory',
        ),
    ]
