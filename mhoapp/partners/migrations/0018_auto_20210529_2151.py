# Generated by Django 3.1.7 on 2021-05-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0017_auto_20210527_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerpage',
            name='phone',
            field=models.TextField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='partnerpage',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
