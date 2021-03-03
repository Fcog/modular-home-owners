# Generated by Django 3.1.7 on 2021-03-03 22:25

from django.db import migrations
import mhoapp.theme.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flexible', '0003_auto_20210303_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexibleonecolumnpage',
            name='body',
            field=wagtail.core.fields.StreamField([('headingH1', mhoapp.theme.models.HeadingH1()), ('headingH2', mhoapp.theme.models.HeadingH2()), ('resourcesCTA', wagtail.core.blocks.StreamBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('WHITE', 'white'), ('BLUE', 'blue')]))])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('text', wagtail.core.blocks.TextBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]
