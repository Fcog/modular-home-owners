# Generated by Django 3.1.7 on 2021-04-19 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('base', '0006_mhosettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mhosettings',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.AlterField(
            model_name='mhosettings',
            name='logo_white',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]