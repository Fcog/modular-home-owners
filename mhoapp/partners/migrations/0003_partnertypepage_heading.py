# Generated by Django 3.1.7 on 2021-05-12 19:21

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_partnertypepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnertypepage',
            name='heading',
            field=wagtail.core.fields.StreamField([('two_columns', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StreamBlock([])), ('column_1', wagtail.core.blocks.StreamBlock([]))], grid_width=12, group='Columns', template='patterns/organisms/sections/two-cols.html'))], default=''),
        ),
    ]
