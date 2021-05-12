# Generated by Django 3.1.7 on 2021-04-26 15:54

from django.db import migrations
import mhoapp.theme.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flexible', '0022_auto_20210426_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexibleonecolumnpage',
            name='body',
            field=wagtail.core.fields.StreamField([('headingH1', mhoapp.theme.blocks.HeadingH1()), ('headingH2', mhoapp.theme.blocks.HeadingH2()), ('resourcesCTA', wagtail.core.blocks.StructBlock([('style', wagtail.core.blocks.ChoiceBlock(choices=[('WH', 'white'), ('BL', 'blue')]))])), ('articlesCTA', wagtail.core.blocks.StructBlock([('introduction', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('column_1_title', wagtail.core.blocks.CharBlock()), ('column_1_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])), ('column_1_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_title', wagtail.core.blocks.CharBlock()), ('column_2_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=False))])), ('hero', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('introduction', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('search_button_text', wagtail.core.blocks.CharBlock(default='Search Homes')), ('filter_bar_text', wagtail.core.blocks.CharBlock(default=''))])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('text', wagtail.core.blocks.TextBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]
