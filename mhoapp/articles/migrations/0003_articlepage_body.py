# Generated by Django 3.1.7 on 2021-03-04 22:26

from django.db import migrations
import mhoapp.theme.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articlepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('headingH2', mhoapp.theme.models.HeadingH2()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('text', wagtail.core.blocks.TextBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]
