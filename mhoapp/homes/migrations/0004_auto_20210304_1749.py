# Generated by Django 3.1.7 on 2021-03-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_priceranges'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priceranges',
            options={'verbose_name_plural': 'price ranges'},
        ),
        migrations.AlterField(
            model_name='priceranges',
            name='range',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
