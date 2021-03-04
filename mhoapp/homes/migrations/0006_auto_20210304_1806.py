# Generated by Django 3.1.7 on 2021-03-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0005_auto_20210304_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priceranges',
            name='range',
        ),
        migrations.AddField(
            model_name='priceranges',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='priceranges',
            name='type',
            field=models.CharField(choices=[('UN', 'Under'), ('OV', 'Over')], default='UN', max_length=2),
        ),
    ]
