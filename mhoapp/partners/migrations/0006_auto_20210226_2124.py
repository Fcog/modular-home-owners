# Generated by Django 3.1.7 on 2021-02-26 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('partners', '0005_typecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='partnertypepage',
            name='type',
        ),
    ]