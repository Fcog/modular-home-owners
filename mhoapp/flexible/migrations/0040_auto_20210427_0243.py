# Generated by Django 3.1.7 on 2021-04-27 02:43

from django.db import migrations
import mhoapp.theme.models
import wagtail.admin.forms.choosers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flexible', '0039_auto_20210426_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexibleonecolumnpage',
            name='body',
            field=wagtail.core.fields.StreamField([('headingH1', mhoapp.theme.blocks.HeadingH1()), ('headingH2', mhoapp.theme.blocks.HeadingH2()), ('articlesCTA', wagtail.core.blocks.StructBlock([('introduction', wagtail.core.blocks.RichTextBlock(features=['bold'])), ('column_1_title', wagtail.core.blocks.CharBlock()), ('column_1_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'])), ('column_1_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_1_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_title', wagtail.core.blocks.CharBlock()), ('column_2_article_1', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_2', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_3', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('column_2_article_4', wagtail.core.blocks.PageChooserBlock(page_type=['articles.ArticlePage'], required=False)), ('button_text', wagtail.core.blocks.CharBlock()), ('button_link', wagtail.core.blocks.StructBlock([('link_to', wagtail.core.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(form_classname='page_link', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', required=False)), ('custom_url', wagtail.core.blocks.CharBlock(form_classname='custom_url_link url_field', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.core.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))])), ('ForumCTA', wagtail.core.blocks.StructBlock([])), ('hero', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('introduction', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('search_button_text', wagtail.core.blocks.CharBlock(default='Search Homes')), ('filter_bar_text', wagtail.core.blocks.CharBlock(default=''))])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('text', wagtail.core.blocks.TextBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], default=''),
        ),
    ]
