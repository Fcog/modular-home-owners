# Generated by Django 3.1.7 on 2021-05-02 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('base', '0020_auto_20210430_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='mhosettings',
            name='homes_ad_button_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Button URL from a page'),
        ),
        migrations.AddField(
            model_name='mhosettings',
            name='homes_ad_button_text',
            field=models.TextField(max_length=255, null=True, verbose_name='Button text'),
        ),
        migrations.AddField(
            model_name='mhosettings',
            name='homes_ad_external_url',
            field=models.URLField(blank=True, null=True, verbose_name='Button external URL'),
        ),
        migrations.AddField(
            model_name='mhosettings',
            name='homes_ad_text',
            field=models.CharField(default='', max_length=254),
        ),
    ]
