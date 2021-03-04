# Generated by Django 3.1.7 on 2021-03-04 01:27

from django.db import migrations
import mhoapp.theme.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flexible', '0004_auto_20210303_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexibleonecolumnpage',
            name='body',
            field=wagtail.core.fields.StreamField([('headingH1', mhoapp.theme.models.HeadingH1()), ('headingH2', mhoapp.theme.models.HeadingH2()), ('resourcesCTA', wagtail.core.blocks.StreamBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('WHITE', 'white'), ('BLUE', 'blue')]))])), ('hero', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock()), ('introduction', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('search_button_text', wagtail.core.blocks.CharBlock(default='Search Homes'))])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('text', wagtail.core.blocks.TextBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]