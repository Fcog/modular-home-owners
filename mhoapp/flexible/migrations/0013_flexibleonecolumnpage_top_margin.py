# Generated by Django 3.1.7 on 2021-05-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexible', '0012_auto_20210521_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexibleonecolumnpage',
            name='top_margin',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
