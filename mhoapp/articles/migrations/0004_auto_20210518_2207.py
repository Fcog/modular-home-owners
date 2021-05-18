# Generated by Django 3.1.7 on 2021-05-18 22:07

from django.db import migrations
import mhoapp.theme.blocks.Separator
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210513_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('separator', mhoapp.theme.blocks.Separator()), ('headingH2', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.StructBlock([('text_size', wagtail.core.blocks.ChoiceBlock(choices=[('normal', 'Normal'), ('large', 'Large')], icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]
