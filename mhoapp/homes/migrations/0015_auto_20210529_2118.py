# Generated by Django 3.1.7 on 2021-05-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0014_auto_20210521_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='floorplans_link',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='link',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
