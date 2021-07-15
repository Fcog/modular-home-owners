# Generated by Django 3.1.7 on 2021-07-13 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('homes', '0016_homesindexpage_initial_home_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylecategory',
            name='style_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='homesindexpage',
            name='initial_home_style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homes.stylecategory', verbose_name='Initial Home Style'),
        ),
    ]
